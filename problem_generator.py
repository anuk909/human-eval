import json
import logging
import os
import random
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any, Union, Tuple, NoReturn

import openai
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)
from tqdm import tqdm
from human_eval.execution import check_correctness


class FileHandler:
    @staticmethod
    def load_file(path: str) -> str:
        return FileHandler._read_file(path)

    @staticmethod
    def load_json_file(path: str) -> Any:
        try:
            return json.loads(FileHandler._read_file(path))
        except json.JSONDecodeError as error:
            logging.error(f"Error loading JSON file: {path}. JSONDecodeError: {error}")
            raise ValueError(
                f"Error loading JSON file: {path}. JSONDecodeError: {error}"
            )

    @staticmethod
    def save_jsonl(path: str, data: Dict[str, Any]) -> None:
        try:
            with open(path, "a") as file:
                json.dump(data, file)
                file.write("\n")
            logging.info(f"Data saved to {path}")
        except Exception as e:
            logging.error(f"Error saving data to {path}: {e}")

    @staticmethod
    def _read_file(path: str) -> str:
        try:
            with open(path, "r") as file:
                return file.read()
        except FileNotFoundError:
            error_message = f"File not found: {path}"
            logging.error(error_message)
            raise ValueError(error_message)


class ProblemValidator:
    def __init__(
        self, example_problem: str, client: openai.AzureOpenAI, config: Dict[str, Any]
    ):
        self.example_problem_dict = json.loads(example_problem)
        self.client = client
        self.config = config

    @property
    def problem_keys(self) -> set:
        return set(self.example_problem_dict.keys())

    def validate_problem(
        self, problem: Dict[str, Any]
    ) -> Dict[str, Union[bool, str, List[str]]]:
        validation_result = {"valid": True, "reason": "", "warnings": []}

        if not self.problem_keys.issubset(problem.keys()):
            return {"valid": False, "reason": "Problem keys mismatch.", "warnings": []}

        self._check_problem_structure(problem, validation_result)
        self._check_correctness(problem, validation_result)
        validation_result["warnings"].extend(self._check_gpt_feedback(problem))

        return validation_result

    def _check_problem_structure(
        self, problem: Dict[str, Any], validation_result: Dict[str, Any]
    ) -> None:
        prompt = problem["prompt"].strip()
        test = problem["test"].strip()

        if not prompt.startswith("def "):
            validation_result["warnings"].append("Prompt does not start with 'def '.")
        if not test.startswith("def "):
            validation_result["warnings"].append("Test does not start with 'def '.")
        if (test_case_count := problem["test"].count("assert")) < 5:
            validation_result["warnings"].append(
                f"Only {test_case_count} test cases found. Minimum recommended is 5."
            )
        if len(prompt) < 50:
            validation_result["warnings"].append("Prompt seems too short.")
        if len(problem["canonical_solution"]) < 10:
            validation_result["warnings"].append("Canonical solution seems too short.")

    def _check_correctness(
        self, problem: Dict[str, Any], validation_result: Dict[str, Any]
    ) -> None:
        try:
            correctness_result = check_correctness(
                problem, problem["canonical_solution"], timeout=15
            )
            if not correctness_result["passed"]:
                validation_result["warnings"].append(
                    "Solution failed correctness check."
                )
        except Exception as error:
            validation_result.update(
                {"valid": False, "reason": f"Error during validation: {error}"}
            )

    def _check_gpt_feedback(self, problem: Dict[str, Any]) -> List[str]:
        system_message = {
            "role": "system",
            "content": (
                "You are an expert in analyzing and critiquing problem statements, especially for coding competitions."
                " Please find and report any potential flaws in this problem. Focus on significant issues that make the problem unusable (focus mainly on the problem and not on the canonical solution or tests). "
                "The output format should be 'severity, flaw_name: description' with each flaw on a new line, severity is between 1 to 5 with 5 being the highest severity."
            ),
        }
        user_message = {"role": "user", "content": json.dumps(problem, indent=2)}

        try:
            completion = self.client.chat.completions.create(
                model=self.config["OPENAI_MODEL"],
                messages=[system_message, user_message],
            )
            gpt_feedback = completion.choices[0].message.content.split("\n")

            feedbacks = []
            for line in gpt_feedback:
                line = line.strip()
                if line:
                    try:
                        severity = int(line[: line.find(",")])
                        if severity >= 4:
                            feedbacks.append(line)
                    except (IndexError, ValueError) as parse_error:
                        logging.warning(
                            f"Unable to parse feedback line: '{line}', Error: {parse_error}"
                        )
            return feedbacks
        except openai.OpenAIError as error:
            return [f"Error getting GPT feedback: {error}"]

    def follow_up_prompt(
        self,
        problem: Dict[str, Any],
        followup_reason: str,
        warnings: List[str],
    ) -> Dict[str, Any]:
        system_message = {
            "role": "system",
            "content": (
                "You are an expert problem setter for advanced coding competitions. You previously created a problem that had the following issues: "
                f"{followup_reason}. Here are some additional issues identified: {warnings}.\n"
                "Please revise and improve the problem statement to fix these issues and return JSON with same keys as the original problem."
            ),
        }
        user_message = {"role": "user", "content": json.dumps(problem, indent=2)}

        try:
            completion = self.client.chat.completions.create(
                model=self.config["OPENAI_MODEL"],
                messages=[system_message, user_message],
                response_format={"type": "json_object"},
            )
            content = completion.choices[0].message.content
            return json.loads(content)
        except (json.JSONDecodeError, openai.OpenAIError) as error:
            logging.error(f"Error during follow-up: {error}")
            raise


class ProblemGenerator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.client = self._setup_openai_client()
        self.example_problem = FileHandler.load_file(
            self.config["EXAMPLE_PROBLEM_PATH"]
        )
        self.cover_story_words = FileHandler.load_json_file(
            self.config["COVER_STORY_PATH"]
        )
        self.topics = FileHandler.load_json_file(self.config["TOPICS_PATH"])
        self.validator = ProblemValidator(self.example_problem, self.client, config)
        self._validate_example_problem()
        self.output_paths = self._setup_output_paths()

    def _setup_openai_client(self) -> openai.AzureOpenAI:
        try:
            return openai.AzureOpenAI(
                api_key=self.config["AZURE_OPENAI_API_KEY"],
                azure_endpoint=self.config["AZURE_OPENAI_ENDPOINT"],
                api_version=self.config["AZURE_OPENAI_API_VERSION"],
            )
        except openai.AuthenticationError as error:
            logging.error(f"Authentication error: {error}")
            raise

    def _validate_example_problem(self) -> None:
        example_validation = self.validator.validate_problem(
            json.loads(self.example_problem)
        )
        if not example_validation["valid"]:
            raise ValueError(
                f"Example problem is invalid, reason: {example_validation['reason']}"
            )
        if example_validation.get("warnings"):
            logging.warning(
                f"Example problem has warnings: {example_validation['warnings']}"
            )

    def _setup_output_paths(self) -> Dict[str, str]:
        timestamp = int(time.time())
        return {
            "new_problems": os.path.join(
                self.config["OUTPUT_DIR"], f"new_problems_{timestamp}.jsonl"
            ),
            "invalid_problems": os.path.join(
                self.config["OUTPUT_DIR"], f"invalid_problems_{timestamp}.jsonl"
            ),
        }

    @property
    def task_id_class(self) -> str:
        task_id = json.loads(self.example_problem).get("task_id")
        return task_id.split("/")[0] if task_id else ""

    def generate_problem(self, task_id: str) -> Dict[str, Any]:
        cover_story_words, topics = random.sample(
            self.cover_story_words, 2
        ), random.sample(self.topics, 2)
        messages = (
            self._get_system_message(),
            self._get_user_message(cover_story_words, topics),
        )

        try:
            completion = self.client.chat.completions.create(
                model=self.config["OPENAI_MODEL"],
                messages=messages,
                response_format={"type": "json_object"},
            )
        except openai.OpenAIError as error:
            logging.error(f"OpenAI error: {error}")
            raise

        content = completion.choices[0].message.content
        try:
            problem_dict = json.loads(content)
        except json.JSONDecodeError as error:
            logging.error(f"Error decoding JSON content: {error}")
            raise

        problem_dict["task_id"] = task_id
        problem_dict["extra_info"] = {
            "cover_story_words": cover_story_words,
            "topics": topics,
            "cleaned_prompt": problem_dict.pop("cleaned_prompt", ""),
        }
        return problem_dict

    def _get_system_message(self) -> ChatCompletionSystemMessageParam:
        return {
            "role": "system",
            "content": (
                "You are an expert problem setter for advanced coding competitions. Create highly novel and complex problems "
                "for the HumanEval Dataset. Requirements:\n"
                f"1. JSON format with keys: {self.validator.problem_keys}.\n"
                f"2. Example: {self.example_problem}\n"
                "3. Prompt must start with 'def' and include examples that will help understanding the problem.\n"
                "4. Test cases must start with 'def' and include at least five complex cases.\n"
                "5. Solution must pass test cases and complete the prompt code without redefining the entry_point function from the prompt.\n"
                "6. Combine multiple concepts uniquely and efficiently.\n"
                "7. Include constraints or twists, and consider time/space complexity requirements.\n"
                "8. The problem should require at least 30 lines to solve.\n"
                "9. Include a 'cleaned_prompt' field that matches the problem prompt but without all the cover story around it, "
                "make sure that the core concept of the questions stays the same and there are some examples and explanations that "
                "makes it easy to understand."
            ),
        }

    def _get_user_message(
        self, cover_story_words: List[str], topics: List[str]
    ) -> ChatCompletionUserMessageParam:
        cover_story_str = " and ".join(cover_story_words)
        topics_str = " and ".join(topics)
        return {
            "role": "user",
            "content": (
                f"Create a problem with a cover story about {cover_story_str} and involving the topics: {topics_str}. "
                "Use concepts from computer vision and ensure complexity and novelty."
            ),
        }

    def save_problem(
        self, problem: Dict[str, Any], is_valid: bool, reason: str = ""
    ) -> None:
        path = self.output_paths["new_problems" if is_valid else "invalid_problems"]
        if not is_valid:
            problem["invalid_reason"] = reason
        FileHandler.save_jsonl(path, problem)


def load_config() -> Dict[str, Any]:
    azure_openai_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    azure_openai_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    if not azure_openai_api_key or not azure_openai_endpoint:
        raise ValueError("AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT must be set.")
    return {
        "AZURE_OPENAI_API_KEY": azure_openai_api_key,
        "AZURE_OPENAI_ENDPOINT": azure_openai_endpoint,
        "AZURE_OPENAI_API_VERSION": "2024-04-01-preview",
        "OPENAI_MODEL": "gpt-4-turbo-2024-04-09",
        "ATTEMPTS": 5,
        "EXAMPLE_PROBLEM_PATH": "resources/example_hard_problem.json",
        "COVER_STORY_PATH": "resources/cover_story_words.json",
        "TOPICS_PATH": "resources/topics.json",
        "OUTPUT_DIR": "data",
    }


def handle_task(problem_generator: ProblemGenerator, attempt: int) -> Any:
    task_id = f"{problem_generator.task_id_class}/{attempt + 1}"
    try:
        new_problem = problem_generator.generate_problem(task_id)
    except Exception as error:
        logging.error(f"Error generating problem for task_id {task_id}: {error}")
        return None, None

    validation_result = problem_generator.validator.validate_problem(new_problem)

    if validation_result["valid"]:
        warnings = validation_result.get("warnings", [])
        if warnings:
            logging.info(
                f"Problem generated for task_id {task_id} with warnings: {warnings}"
            )
            extra_info = new_problem.pop("extra_info")
            extra_info["warnings"] = warnings

            # Attempt to improve the problem due to warnings
            followup_reason = "Problem is valid but has the following warnings."
            try:
                improved_problem = problem_generator.validator.follow_up_prompt(
                    new_problem, followup_reason, warnings
                )
                improved_problem["extra_info"]["cover_story_words"] = extra_info[
                    "cover_story_words"
                ]
                improved_problem["extra_info"]["topics"] = extra_info["cleaned_prompt"]
                improved_validation_result = (
                    problem_generator.validator.validate_problem(improved_problem)
                )
                if improved_validation_result["valid"]:
                    improved_warnings = improved_validation_result.get("warnings", [])
                    if improved_warnings:
                        logging.info(
                            f"Improved problem generated for task_id {task_id} with warnings: {improved_warnings}"
                        )
                        improved_problem["extra_info"]["warnings"] = improved_warnings
                    return improved_problem, None
                else:
                    improved_reason = improved_validation_result["reason"]
                    logging.warning(
                        f"Improved problem invalid for task_id {task_id}, reason: {improved_reason}"
                    )
                    improved_problem["invalid_reason"] = improved_reason
                    return None, improved_problem
            except Exception as error:
                logging.error(
                    f"Error during follow-up prompt for task_id {task_id}: {error}"
                )
                new_problem["invalid_reason"] = f"Valid with warnings: {warnings}"
                return new_problem, None
        else:
            logging.info(f"Problem generated for task_id {task_id}")
            return new_problem, None
    else:
        reason = validation_result["reason"]
        warnings = validation_result.get("warnings", [])
        logging.warning(
            f"Problem invalid for task_id {task_id}, reason: {reason}, warnings: {warnings}"
        )

        followup_reason = f"{reason}; Ensure all given topics are used and the problem statement is understandable."

        try:
            improved_problem = problem_generator.validator.follow_up_prompt(
                new_problem, followup_reason, warnings
            )
            improved_validation_result = problem_generator.validator.validate_problem(
                improved_problem
            )
            if improved_validation_result["valid"]:
                warnings = improved_validation_result.get("warnings", [])
                if warnings:
                    logging.info(
                        f"Improved problem generated for task_id {task_id} with warnings: {warnings}"
                    )
                    improved_problem["extra_info"]["warnings"] = warnings
                return improved_problem, None
            else:
                improved_reason = improved_validation_result["reason"]
                logging.warning(
                    f"Improved problem invalid for task_id {task_id}, reason: {improved_reason}"
                )
                improved_problem["invalid_reason"] = improved_reason
                return None, improved_problem
        except Exception as error:
            logging.error(
                f"Error during follow-up prompt for task_id {task_id}: {error}"
            )
            new_problem["invalid_reason"] = reason
            return None, new_problem


def main() -> None:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    config = load_config()
    problem_generator = ProblemGenerator(config)

    valid_problems = []
    invalid_problems_counter = defaultdict(int)

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(handle_task, problem_generator, attempt)
            for attempt in range(config["ATTEMPTS"])
        ]
        for future in tqdm(
            as_completed(futures), total=config["ATTEMPTS"], desc="Generating problems"
        ):
            new_problem, invalid_problem = future.result()
            if new_problem:
                problem_generator.save_problem(new_problem, is_valid=True)
                valid_problems.append(new_problem)
            elif invalid_problem:
                problem_generator.save_problem(
                    invalid_problem,
                    is_valid=False,
                    reason=invalid_problem["invalid_reason"],
                )
                invalid_problems_counter[invalid_problem["invalid_reason"]] += 1

    logging.info(
        f"Problem generation completed. Created {len(valid_problems)} valid problems from {config['ATTEMPTS']} attempts"
    )
    if invalid_problems_counter:
        logging.info(f"Validation failures: {dict(invalid_problems_counter)}")


if __name__ == "__main__":
    main()

import json
import logging
import os
import random
import time
from collections import defaultdict
from typing import List, Dict, Any, Union
from tqdm import tqdm

import openai
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

from human_eval.execution import check_correctness


class ProblemGenerator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.client = self.setup_openai_client()
        self.example_problem = self.load_file(self.config["EXAMPLE_PROBLEM_PATH"])
        self.validate_example_problem()
        self.cover_story_words = self.load_json_file(self.config["COVER_STORY_PATH"])
        self.topics = self.load_json_file(self.config["TOPICS_PATH"])
        timestamp = int(time.time())
        self.new_problems_path = os.path.join(
            self.config["OUTPUT_DIR"], f"new_problems_{timestamp}.jsonl"
        )
        self.invalid_problems_path = os.path.join(
            self.config["OUTPUT_DIR"], f"invalid_problems_{timestamp}.jsonl"
        )

    def setup_openai_client(self) -> openai.AzureOpenAI:
        try:
            return openai.AzureOpenAI(
                api_key=self.config["AZURE_OPENAI_API_KEY"],
                azure_endpoint=self.config["AZURE_OPENAI_ENDPOINT"],
                api_version=self.config["AZURE_OPENAI_API_VERSION"],
            )
        except openai.AuthenticationError as e:
            logging.error(f"Authentication error: {e}")
            raise

    @property
    def example_problem_dict(self) -> Dict[str, Any]:
        return json.loads(self.example_problem)

    def load_file(self, path: str) -> str:
        try:
            with open(path, "r") as f:
                return f.read()
        except FileNotFoundError:
            logging.error(f"File not found: {path}")
            raise

    def load_json_file(self, path: str) -> List[str]:
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"JSON file not found: {path}")
            raise

    @property
    def problem_keys(self) -> set:
        return set(self.example_problem_dict.keys())

    @property
    def task_id_class(self) -> str:
        task_id = self.example_problem_dict.get("task_id")
        return task_id.split("/")[0] if task_id else ""

    def validate_example_problem(self) -> None:
        example_validation = self.validate_problem(
            self.example_problem_dict, f"{self.task_id_class}/0"
        )
        if not example_validation["valid"]:
            logging.error(
                f"Example problem is invalid, reason - {example_validation['reason']}"
            )
            raise ValueError("Example problem is invalid")

    def generate_problem(self, task_id: str) -> Dict[str, Any]:
        cover_story_words = random.sample(self.cover_story_words, 2)
        topics = random.sample(self.topics, 2)

        messages = (
            self.get_system_message(),
            self.get_user_message(cover_story_words, topics),
        )

        try:
            completion = self.client.chat.completions.create(
                model=self.config["OPENAI_MODEL"],
                messages=messages,
                response_format={"type": "json_object"},
            )
        except openai.OpenAIError as e:
            logging.error(f"OpenAI error: {e}")
            raise

        content = completion.choices[0].message.content
        try:
            problem_dict = json.loads(content)
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON content: {e}")
            raise

        problem_dict["task_id"] = task_id
        extra_info = {
            "cover_story_words": cover_story_words,
            "topics": topics,
            "cleaned_prompt": problem_dict.pop("cleaned_prompt", ""),
        }
        problem_dict["extra_info"] = extra_info
        return problem_dict

    def get_system_message(self) -> ChatCompletionSystemMessageParam:
        return {
            "role": "system",
            "content": (
                "You are an expert problem setter for advanced coding competitions. Create highly novel and complex problems for the HumanEval Dataset. Requirements:\n"
                f"1. JSON format with keys: {str(self.problem_keys)}.\n"
                f"2. Example: {self.example_problem}\n"
                "3. Prompt must start with 'def'.\n"
                "4. Test cases must start with 'def' and include at least five complex cases.\n"
                "5. Solution must pass test cases.\n"
                "6. Combine multiple concepts uniquely and efficiently.\n"
                "7. Include constraints or twists, and consider time/space complexity requirements.\n"
                "8. Include a 'cleaned_prompt' field that matches the problem prompt but without all the cover story around it, "
                "make sure that the core concept of the questions stays the same."
            ),
        }

    def get_user_message(
        self, cover_story_words: List[str], topics: List[str]
    ) -> ChatCompletionUserMessageParam:
        cover_story_str = " and ".join(cover_story_words)
        topics_str = ", ".join(topics)
        return {
            "role": "user",
            "content": (
                f"Create a problem with a cover story about {cover_story_str} and involving the topics: {topics_str}. Ensure complexity and novelty."
            ),
        }

    def validate_problem(
        self, problem: Dict[str, Any], task_id: str
    ) -> Dict[str, Union[bool, str]]:
        validation_result = {"valid": False, "reason": ""}

        if not self.problem_keys.issubset(problem.keys()):
            validation_result["reason"] = "Problem keys mismatch."
            return validation_result

        if problem["task_id"] != task_id:
            validation_result["reason"] = "Task ID mismatch."
            return validation_result

        try:
            if not problem["prompt"].startswith("def "):
                validation_result["reason"] = "Prompt does not start with 'def '."
                return validation_result

            if not problem["test"].startswith("def "):
                validation_result["reason"] = "Test does not start with 'def '."
                return validation_result

            if problem["test"].count("assert") < 5:
                validation_result["reason"] = "Fewer than 5 test cases."
                return validation_result

            correctness_result = check_correctness(
                problem, problem["canonical_solution"], timeout=10
            )
            if not correctness_result["passed"]:
                validation_result["reason"] = "Solution failed correctness check."
                return validation_result

            validation_result["valid"] = True
            return validation_result
        except Exception as e:
            validation_result["reason"] = f"Error during validation: {e}"
            return validation_result

    def save_problem(self, problem: Dict[str, Any]) -> None:
        try:
            with open(self.new_problems_path, "a") as f:
                json.dump(problem, f)
                f.write("\n")
            logging.info(f"New problem saved to {self.new_problems_path}")
        except Exception as e:
            logging.error(f"Error saving problem to {self.new_problems_path}: {e}")

    def save_invalid_problem(self, problem: Dict[str, Any], reason: str) -> None:
        try:
            with open(self.invalid_problems_path, "a") as f:
                json.dump({"reason": reason, "problem": problem}, f)
                f.write("\n")
            logging.info(f"Invalid problem saved to {self.invalid_problems_path}")
        except Exception as e:
            logging.error(f"Error saving invalid problem: {e}")


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


def main() -> None:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    config = load_config()
    problem_generator = ProblemGenerator(config)

    problems: List[Dict[str, Any]] = []
    invalid_problems_counter: Dict[str, int] = defaultdict(int)

    for _ in tqdm(range(config["ATTEMPTS"]), desc="generating problems"):
        task_id = f"{problem_generator.task_id_class}/{len(problems) + 1}"

        try:
            new_problem = problem_generator.generate_problem(task_id)
            validation_result = problem_generator.validate_problem(new_problem, task_id)
        except Exception as e:
            logging.error(f"Error generating problem for task_id {task_id}: {e}")
            continue

        if validation_result["valid"]:
            logging.info(f"Valid problem generated for task_id {task_id}")
            problem_generator.save_problem(new_problem)
            problems.append(new_problem)
        else:
            reason = validation_result["reason"]
            logging.warning(f"Invalid problem generated, reason: {reason}")
            problem_generator.save_invalid_problem(new_problem, reason)
            invalid_problems_counter[reason] += 1

    logging.info(
        f"Problem generation completed. Created {len(problems)} valid problems from {config['ATTEMPTS']} attempts"
    )
    if invalid_problems_counter:
        logging.info(f"Validation failures: {list(invalid_problems_counter.items())}")


if __name__ == "__main__":
    main()

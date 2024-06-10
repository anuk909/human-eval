import json
import logging
import os
import random
import time
from tqdm import tqdm
from collections import defaultdict
from typing import List, Dict, Any

import openai
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)
from human_eval.execution import check_correctness


class ProblemGenerator:
    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.client = self.setup_openai_client()
        self.example_problem = self.load_example_problem()
        self.validate_example_problem()

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
    def example_problem_dict(self) -> Dict[str, str]:
        return json.loads(self.example_problem)

    def load_example_problem(self) -> str:
        try:
            with open(self.config["EXAMPLE_PROBLEM_PATH"], "r") as f:
                return f.read()
        except FileNotFoundError:
            logging.error(
                f"Example problem file not found: {self.config['EXAMPLE_PROBLEM_PATH']}"
            )
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
            self.example_problem, self.task_id_class + "/0"
        )
        if not example_validation["valid"]:
            logging.error(
                f"Example problem is invalid, reason - {example_validation['reason']}"
            )
            raise ValueError("Example problem is invalid")

    def generate_problem(self, task_id: str, reference_problems: List[str]) -> str:
        messages = (
            self.get_system_message(),
            self.get_user_message(task_id, reference_problems),
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
        return content if content else ""

    def get_system_message(self) -> ChatCompletionSystemMessageParam:
        return {
            "role": "system",
            "content": (
                "You are a writer of new problems for the HumanEval Dataset. Your task is to create a high-quality problem that meets the following requirements:\n\n"
                f"1. The response should be in JSON format, following the same structure as the existing HumanEval problems (the keys are: {str(self.problem_keys)}).\n"
                f"2. Provide an example problem in the same format as the one given: {self.example_problem}\n\n"
                "3. The problem prompt must start with 'def'.\n"
                "4. The test cases must also start with 'def'.\n" 
                "5. The canonical solution must pass all the test cases.\n"
                "6. Include at least 5 different test cases.\n"
                "7. Avoid mathematical problems."
            )
        }


    def get_user_message(
        self, task_id: str, reference_problems: List[str]
    ) -> ChatCompletionUserMessageParam:
        return {
            "role": "user",
            "content": f"Generate new and unique problem with task_id {task_id} in HumanEval, it should be different than any problem in the current problems: "
            + "\n".join(reference_problems),
        }

    def validate_problem(self, problem: str, task_id: str) -> Dict[str, Any]:
        validation_result = {"valid": False, "reason": ""}

        try:
            problem_dict = json.loads(problem)
        except json.JSONDecodeError as e:
            validation_result["reason"] = f"Invalid JSON format for problem: {e}"
            return validation_result

        if self.problem_keys != set(problem_dict):
            return validation_result

        if problem_dict["task_id"] != task_id:
            validation_result["reason"] = "Task ID mismatch."
            return validation_result

        if not problem_dict["prompt"].startswith("def "):
            validation_result["reason"] = "Prompt does not start with 'def '"
            return validation_result

        if not problem_dict["test"].startswith("def "):
            validation_result["reason"] = "Test does not start with 'def '"
            return validation_result

        if problem_dict["test"].count("assert") < 5:
            validation_result["reason"] = "Less than 5 test cases"
            return validation_result

        try:
            correctness_result = check_correctness(
                problem_dict, problem_dict["canonical_solution"], timeout=10
            )
            if not correctness_result["passed"]:
                validation_result["reason"] = (
                    f"Solution failed correctness check. correctness_check_result: {correctness_result['result']}"
                )
                return validation_result
        except Exception as e:
            validation_result["reason"] = f"Error during correctness check: {e}"
            return validation_result

        validation_result["valid"] = True
        return validation_result

    def save_problem(self, problem: str) -> None:
        try:
            with open(self.new_problems_path, "a") as f:
                f.write(problem + "\n")
            logging.info(f"New problem saved to {self.new_problems_path}")
        except Exception as e:
            logging.error(f"Error saving problem to {self.new_problems_path}: {e}")

    def save_invalid_problem(self, problem: str, reason: str) -> None:
        try:
            with open(self.invalid_problems_path, "a") as f:
                f.write(json.dumps({"reason": reason, "problem": problem}) + "\n")
            logging.info(
                f"Invalid problem and reason saved to {self.invalid_problems_path}"
            )
        except Exception as e:
            logging.error(
                f"Error saving problem and reason to {self.invalid_problems_path}: {e}"
            )


def load_config() -> Dict[str, Any]:
    azure_openai_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    azure_openai_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")

    if azure_openai_api_key is None or azure_openai_endpoint is None:
        raise ValueError(
            "AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT environment variables must be set."
        )

    config = {
        "AZURE_OPENAI_API_KEY": azure_openai_api_key,
        "AZURE_OPENAI_ENDPOINT": azure_openai_endpoint,
        "AZURE_OPENAI_API_VERSION": "2024-04-01-preview",
        "OPENAI_MODEL": "gpt-4-turbo-2024-04-09",
        "ATTEMPTS": 5,
        "MAX_REFERENCE_PROBLEMS": 10,
        "EXAMPLE_PROBLEM_PATH": "data/example_hard_problem.jsonl",
        "OUTPUT_DIR": "data",
    }
    return config


def main() -> None:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    config = load_config()
    problem_generator = ProblemGenerator(config)

    problems: List[str] = []
    invalid_problems_counter: Dict[str, int] = defaultdict(int)
    for _ in tqdm(range(config["ATTEMPTS"]), desc="generating problems"):
        task_id = f"{problem_generator.task_id_class}/{len(problems) + 1}"
        reference_problems = problems + [problem_generator.example_problem]
        if len(reference_problems) > 10:
            reference_problems = random.sample(reference_problems, 10)

        try:
            new_problem = problem_generator.generate_problem(
                task_id, reference_problems
            )
            validation_result = problem_generator.validate_problem(new_problem, task_id)
            new_problem = json.dumps(json.loads(new_problem))
        except Exception as e:
            logging.error(f"Error generating problem for task_id {task_id}: {e}")
            continue

        if validation_result["valid"]:
            logging.info(f"Valid problem generated for task_id {task_id}")
            problem_generator.save_problem(new_problem)
            problems.append(new_problem)
        else:
            reason = validation_result["reason"]
            logging.warning(
                f"Invalid problem for task_id {task_id}: {new_problem}, reason: {reason}"
            )
            problem_generator.save_invalid_problem(new_problem, reason)
            invalid_problems_counter[reason] += 1

    logging.info(
        f"Problem generation completed. Created {len(problems)} new valid problems out of {config['ATTEMPTS']} attempts"
    )
    if invalid_problems_counter:
        logging.info(
            f"Validation failed reasons: {list(invalid_problems_counter.items())}"
        )


if __name__ == "__main__":
    main()

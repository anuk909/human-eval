import json
import logging
import os
import random
from typing import List, Dict
import time
from tqdm import tqdm
from collections import defaultdict

import openai
from human_eval.execution import check_correctness


class ProblemGenerator:
    def __init__(self, config):
        self.config = config
        self.client = self.setup_openai_client()
        self.example_problem = self.load_example_problem()
        self.problem_keys = self.extact_problem_keys()
        example_validation = self.validate_problem(self.example_problem)
        if not example_validation["valid"]:
            logging.error(
                f"Example problem is invalid, reason - {example_validation['reason']}"
            )
            raise ValueError("Example problem is invalid")

        timestamp = int(time.time())
        self.new_problems_path = os.path.join(
            self.config["OUTPUT_DIR"], f"new_problems_{timestamp}.jsonl"
        )
        self.invalid_problems_path = os.path.join(
            self.config["OUTPUT_DIR"], f"invalid_problems_{timestamp}.jsonl"
        )

    def setup_openai_client(self):
        try:
            return openai.AzureOpenAI(
                api_key=self.config["AZURE_OPENAI_API_KEY"],
                azure_endpoint=self.config["AZURE_OPENAI_ENDPOINT"],
                api_version=self.config["AZURE_OPENAI_API_VERSION"],
            )
        except openai.error.AuthenticationError as e:
            logging.error(f"Authentication error: {e}")
            raise

    def load_example_problem(self):
        try:
            with open(self.config["EXAMPLE_PROBLEM_PATH"], "r") as f:
                return f.read()
        except FileNotFoundError:
            logging.error(
                f"Example problem file not found: {self.config['EXAMPLE_PROBLEM_PATH']}"
            )
            raise

    def extact_problem_keys(self):
        return set(json.loads(self.example_problem).keys())

    def generate_problem(self, task_id: str, reference_problems: List[Dict]) -> str:
        messages = [
            {
                "role": "system",
                "content": f"You are a Writer of new problems for the HumanEval Dataset. "
                f"Your response should be in JSON format in the same format as HumanEval (the keys are - {str(self.problem_keys)}), "
                f"for example, here is one problem: {self.example_problem}"
                "The prompt must start with def, the test must start with def, canonical_solution must solve the test, there should be at least least 5 different test cases",
            },
            {
                "role": "user",
                "content": f"Generate new and unique problem with task_id {task_id} in HumanEval, it should be different than any problem in the current problems: "
                + "\n".join(reference_problems),
            },
        ]

        try:
            completion = self.client.chat.completions.create(
                model=self.config["OPENAI_MODEL"],
                messages=messages,
                response_format={"type": "json_object"},
            )
        except openai.error.OpenAIError as e:
            logging.error(f"OpenAI error: {e}")
            raise

        return completion.choices[0].message.content

    def validate_problem(self, problem: str, task_id: str = None) -> Dict:
        validation_result = {"valid": False, "reason": ""}

        # Attempt to load the problem as JSON
        try:
            problem = json.loads(problem)
        except json.JSONDecodeError as e:
            validation_result["reason"] = f"Invalid JSON format for problem: {e}"
            return validation_result

        if self.problem_keys != set(problem):
            validation_result["reason"] = (
                f"Missing required keys: {','.join(self.problem_keys - set(problem))}"
            )
            return validation_result

        if task_id and problem["task_id"] != task_id:
            validation_result["reason"] = "Task ID mismatch."
            return validation_result

        if not problem["prompt"].startswith("def "):
            validation_result["reason"] = (
                "Prompt function definition must start with 'def '."
            )
            return validation_result

        if not problem["test"].startswith("def "):
            validation_result["reason"] = (
                "Test function definition must start with 'def '."
            )
            return validation_result

        if problem["test"].count("assert") < 5:
            validation_result["reason"] = (
                "The problem must have at least 5 different test cases"
            )
            return validation_result

        try:
            correctness_result = check_correctness(
                problem, problem["canonical_solution"], timeout=10
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

    def save_problem(self, problem: str):
        try:
            with open(self.new_problems_path, "a") as f:
                f.write(problem + "\n")
            logging.info(f"New problem saved to {self.new_problems_path}")
        except Exception as e:
            logging.error(f"Error saving problem to {self.new_problems_path}: {e}")

    def save_invalid_problem(self, problem: str, reason: str):
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


def load_config():
    config = {
        "AZURE_OPENAI_API_KEY": os.environ.get("AZURE_OPENAI_API_KEY"),
        "AZURE_OPENAI_ENDPOINT": os.environ.get("AZURE_OPENAI_ENDPOINT"),
        "AZURE_OPENAI_API_VERSION": "2024-04-01-preview",
        "OPENAI_MODEL": "gpt-4-turbo-2024-04-09",
        "ATTEMPTS": 5,
        "MAX_REFERENCE_PROBLEMS": 10,
        "EXAMPLE_PROBLEM_PATH": "data/example_hard_problem.jsonl",
        "OUTPUT_DIR": "data",
    }
    return config


def main():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    config = load_config()
    problem_generator = ProblemGenerator(config)

    problems = []
    invalid_problems_counter = defaultdict(int)
    for _ in tqdm(range(config["ATTEMPTS"]), desc="generating problems"):
        task_id = f"hard/{len(problems) + 1}"
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

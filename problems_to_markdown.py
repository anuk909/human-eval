import json
import os
import argparse
import textwrap

def json_to_markdown(json_data):
    task_id = json_data["task_id"]
    prompt = json_data["prompt"]
    canonical_solution = json_data["canonical_solution"]
    test_cases = json_data["test"]
    entry_point = json_data["entry_point"]

    markdown = f"# Task ID: {task_id}\n\n"
    markdown += "## Prompt\n\n"
    markdown += f"```python\n{prompt}\n```\n\n"
    markdown += "## Canonical Solution\n\n"
    markdown += f"```python\n{canonical_solution}\n```\n\n"
    markdown += "## Test Cases\n\n"
    markdown += f"```python\n{test_cases}\n```\n\n"
    markdown += f"## Entry Point\n\n`{entry_point}`\n\n"

    return markdown

def convert_jsonl_to_markdown(input_file, output_dir, include_invalid=False):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    with open(input_file, "r") as f:
        line_counter = 0
        for line in f:
            json_data = json.loads(line)
            is_invalid = "problem" in json_data and "reason" in json_data

            if is_invalid and not include_invalid:
                continue  # Skip invalid problems if not included

            problem_json = json_data if not is_invalid else json.loads(json_data["problem"])
            task_class, task_id = problem_json["task_id"].split("/")
            output_task_dir = os.path.join(output_dir, task_class)
            os.makedirs(output_task_dir, exist_ok=True)

            markdown_content = json_to_markdown(problem_json)

            if is_invalid:
                reason = json_data["reason"]
                reason_md = f"## Reason\n\n```\n{textwrap.dedent(reason).strip()}\n```\n\n"
                invalid_md = reason_md + markdown_content

                output_file = os.path.join(output_task_dir, f"line_{line_counter}_invalid.md")
            else:
                output_file = os.path.join(output_task_dir, f"{task_id}.md")

            with open(output_file, "w") as out_f:
                out_f.write(invalid_md if is_invalid else markdown_content)

            line_counter += 1
            print(f"Markdown file '{output_file}' created successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSONL to Markdown files")
    parser.add_argument("input_file", help="Path to the input JSONL file")
    parser.add_argument("output_dir", help="Path to the output directory for Markdown files")
    parser.add_argument("--include-invalid", action="store_true", help="Include invalid problems in the output")
    args = parser.parse_args()

    convert_jsonl_to_markdown(args.input_file, args.output_dir, args.include_invalid)
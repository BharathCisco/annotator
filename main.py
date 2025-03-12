import sys
import os
import json
import ast
from collections import defaultdict

# Dictionary to store variable types per file
variable_types = defaultdict(lambda: defaultdict(set))


def trace_calls(frame, event, arg):
    if event != "call":
        return
    return trace_lines


def trace_lines(frame, event, arg):
    if event != "line":
        return
    local_vars = frame.f_locals
    filename = frame.f_code.co_filename
    if filename.endswith(".py") and not filename.startswith("<"):
        for var, value in local_vars.items():
            variable_types[filename][var].add(type(value).__name__)
    return trace_lines


def analyze_project(directory):
    python_files = [os.path.join(root, file)
                    for root, _, files in os.walk(directory)
                    for file in files if file.endswith(".py")]

    for py_file in python_files:
        try:
            with open(py_file, "r", encoding="utf-8") as f:
                code = f.read()
                tree = ast.parse(code)
                exec(compile(tree, py_file, "exec"), {})
        except Exception as e:
            print(f"Error processing {py_file}: {e}")

    report = {file: {var: list(types) for var, types in vars.items()} for file, vars in variable_types.items()}
    with open("annotations_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print("Annotations report saved to annotations_report.json")


if __name__ == "__main__":
    sys.settrace(trace_calls)
    project_dir = input("Enter the path to the Python project: ").strip()
    analyze_project(project_dir)

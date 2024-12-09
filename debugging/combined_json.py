# Path to the folder containing the Python files
import glob
import os
import json
import re

python_files = glob.glob(os.path.join(
    "LLM-Improved-Code-Quality/test_data/temp2/code/python", '*.py'))
java_files = glob.glob(os.path.join(
    "LLM-Improved-Code-Quality/test_data/temp2/code/java", '*.java'))
leetcode_tasks_path = "LLM-Improved-Code-Quality/test_data/temp2/leetcode_tasks/leetcode.json"

pylint_reports = "LLM-Improved-Code-Quality/test_data/temp2/reports/python/pylint/"
flake8_reports = "LLM-Improved-Code-Quality/test_data/temp2/reports/python/flake8/"
pmd_reports = "LLM-Improved-Code-Quality/test_data/temp2/reports/java/pmd/"
checkstyle_reports = "LLM-Improved-Code-Quality/test_data/temp2/reports/java/checkstyle/"

combined_json_path = "LLM-Improved-Code-Quality/test_data/temp2/leetcode_tasks/task_info.json"

combined_json = []

with open(leetcode_tasks_path, 'r') as f:
    leetcode_list = json.load(f)

for python_file_path, java_file_path in zip(python_files, java_files):
    with open(python_file_path, 'r') as python_file, open(java_file_path, 'r') as java_file:
        task_meta = {}

        file_name = python_file.name.split("\\")[-1]
        task_meta['id'] = file_name.split("-")[0]
        # task_meta['name'] = re.search(r'\d+-(.*)\.py', file_name)

        data_info = next(
            (item for item in leetcode_list if item["id"] == task_meta['id']), None)
        task_meta.update(data_info)

        task_meta['python_code'] = python_file.read()

        with open(pylint_reports + file_name.split(".")[0] + ".txt", 'r') as f:
            task_meta['pylint_report'] = f.read()
        
        with open(flake8_reports + file_name.split(".")[0] + ".txt", 'r') as f:
            task_meta['flake8_report'] = f.read()

        task_meta['java_code'] = java_file.read()

        with open(pmd_reports + file_name.split(".")[0] + ".txt", 'r') as f:
            task_meta['pmd_report'] = f.read()

        with open(checkstyle_reports + file_name.split(".")[0] + ".txt", 'r') as f:
            task_meta['checkstyle_report'] = f.read()

        print("Modifying code with Groq...", task_meta)

        combined_json.append(task_meta)

with open(combined_json_path, 'w') as f:
    json.dump(combined_json, f)
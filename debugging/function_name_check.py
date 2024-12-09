import glob
import json
import os
import re
from time import sleep

python_files = glob.glob(os.path.join(
    "LLM-Improved-Code-Quality/test_data/temp2/updated_code/code2/python", '*.py'))
java_files = glob.glob(os.path.join(
    "LLM-Improved-Code-Quality/test_data/temp2/updated_code/code2/java", '*.java'))

leetcode_tasks_path = "LLM-Improved-Code-Quality/test_data/temp2/leetcode_tasks/leetcode.json"

with open(leetcode_tasks_path, 'r') as f:
    leetcode_list = json.load(f)

for python_file_path, java_file_path in zip(python_files, java_files):

    with open(python_file_path, 'r') as python_file, open(java_file_path, 'r') as java_file:
        python_code = python_file.read()
        java_code = java_file.read()

        file_name = python_file.name.split("\\")[-1]
        task_id = file_name.split("-")[0]

        print(task_id)

        data_info = next(
            (item for item in leetcode_list if item["id"] == task_id))

        # Extract the function name from `python_template`
        python_template = data_info["python_template"]
        python_function_name = re.search(r"def (\w+)\s?\(", python_template).group(0)

       # Java Code: Extract the method name from `java_template`
        java_template = data_info["java_template"]
        java_method_name = re.search(
            r"public .* (\w+)\s?\(", java_template).group(0)
        
        print(java_method_name)

        # Replace the function name in the Python code
        python_code = re.sub(
            r"def (\w+)\s?\(", f"{python_function_name}", python_code, count=1)
        
        # Replace the method name in the Java code
        java_code = re.sub(r"public .* (\w+)\s?\(",
                           f"{java_method_name}", java_code, count=1)
        

        sleep(5)
        
        # Save the updated Python code back to the file
        # with open(python_file_path, 'w') as python_file, open(java_file_path, 'w') as java_file:
        #     python_file.write(python_code)
        #     java_file.write(java_code)
        
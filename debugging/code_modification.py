import glob
import json
import os
import re
from time import sleep
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY2")

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def get_groq_llama_response(messages, model='llama3-8b-8192'):
    """
    Returns the response from the Llama model using Groq for a given prompt.
    """
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        stop="```",
        # temperature=0.0
    )

    return chat_completion.choices[0].message.content


def modify_code(output_dir, lang, task_meta):
    """
    Generates code from Llama for a given code task.
    """

    task_id = task_meta['id']
    task_name = task_meta['name']
    task_description = task_meta['task_description']
    test_cases = task_meta['test_cases']
    python_code = task_meta['python_code']
    python_template = task_meta['python_template']
    java_code = task_meta['java_code']
    java_template = task_meta['java_template']
    flake8_report = task_meta['flake8_report']
    pylint_report = task_meta['pylint_report']
    pmd_report = task_meta['pmd_report']
    checkstyle_report = task_meta['checkstyle_report']

    python_system_prompt = f"You are a senior level software engineer. One of the naive developer written some code which failed through pass ruleset. Modify the code to solve issues based on description and reports. You have to follow the template as per company policy. You cannot change the class and method names.\n"

    if lang == "Python":

        messages = [
            {"role": "system", "content": python_system_prompt},
            {"role": "user", "content": f"Modify the below {lang} code to increase the code-quality for the task given in description and solve issues mentioned in the reports. Make Sure it passes all the sample test-cases. \n "
             f"Code: {python_code}\n, description: {task_description}\n, test_cases: {test_cases}, code_template: {python_template}\n, Flake8_report: {flake8_report}\n, Pylint_report: {pylint_report}\n"
             },
            {"role": "assistant", "content": "```Python"}
        ]

    else:

        java_system_prompt = f"You are a senior level software engineer. One of the naive developer written some code which failed through pass ruleset. Modify the code to solve issues based on description and reports. You have to follow the template as per company policy. You cannot change the class and method names.\n"

        messages = [
            {"role": "system", "content": java_system_prompt},
            {"role": "user", "content": f"Modify the below {lang} code to increase the code-quality for the task given in description and solve issues mentioned in the reports. Make Sure it passes all the sample test-cases.\n"
             f"Code: {java_code}\n, description: {task_description}\n, test_cases: {test_cases}, code_template: {java_template}\n, pmd_report: {pmd_report}\n, checkstyle_report: {checkstyle_report}\n"
             },
            {"role": "assistant", "content": "```Java"}
        ]

    # response = get_llama_response(messages)
    response = get_groq_llama_response(messages)

    # print(response)

    sleep(2)

    # code = get_code_from_response(
    #     response, lang)

    print(f"{task_id}-{task_name}-{lang}\n",
          response, "\n")

    if lang == "Python":
        output_file = os.path.join(
            output_dir + lang, f"{task_id}-{task_name}.py")
    else:
        output_file = os.path.join(
            output_dir + lang, f"{task_id}-{task_name}.java")

    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(response)


# def get_code_from_response(text, language):

#     if "```" not in text:
#         return text.strip()

#     # Make the language check case-insensitive
#     if re.search(fr"```{language}", text, re.IGNORECASE):
#         # Use a case-insensitive pattern to capture code blocks for the specified language
#         pattern = rf'```{language}(.*?)```'
#     else:
#         # Fallback to a generic code block pattern
#         pattern = r'```(.*?)```'

#     # Find all matching code blocks (case-insensitive for the specified language)
#     code_blocks = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)

#     return ''.join(code_blocks).strip()


if __name__ == "__main__":

    task_info_path = "LLM-Improved-Code-Quality/test_data/temp2/leetcode_tasks/task_info.json"

    with open(task_info_path, "r") as openfile:
        task_meta = json.load(openfile)

    output_dir = "LLM-Improved-Code-Quality/test_data/temp2/updated_code/code2/"

    i = 0

    for task in task_meta:
        if i <= 200:
            modify_code(output_dir, "Python", task)
            modify_code(output_dir, "Java", task)
        else:
            break
        i += 1

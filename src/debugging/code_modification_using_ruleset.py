import glob
import json
import os
import re
from groq import Groq

# Groq API key: "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"
# Grow API key2: "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"
# Groq API key3: "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"
# Groq API key4: "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"
# Groq API key5: "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"

os.environ["GROQ_API_KEY"] = "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"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def get_groq_llama_response(messages, model='llama3-8b-8192'):
    """
    Returns the response from the Llama model using Groq for a given prompt.
    """
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content


def modify_code(output_dir, lang, task_meta):
    """
    Generates code from Llama for a given code task.
    """

    task_id = task_meta['id']
    task_name = task_meta['name']
    task_description = task_meta['task_description']
    python_code = task_meta['python_code']
    java_code = task_meta['java_code']
    flake8_report = task_meta['flake8_report']
    pylint_report = task_meta['pylint_report']
    pmd_report = task_meta['pmd_report']
    checkstyle_report = task_meta['checkstyle_report']

    system_prompt = f"Modify the code to solve issues based on description and reports.\n{task_description}"

    if lang == "python":

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Modify the {lang} below code to solve issues.\n"
             f"Code: {python_code}\n, description: {task_description} , Flake8_report: {flake8_report}\n, Pylint_report: {pylint_report}"}
        ]

    else:

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Modify the {lang} below code to solve issues.\n"
             f"Code: {java_code}\n, description: {task_description} , pmd_report: {pmd_report}\n, checkstyle_report: {checkstyle_report}"}
        ]

    # response = get_llama_response(messages)
    response = get_groq_llama_response(messages)

    code = get_code_from_response(
        response, lang)

    print(f"{task_id} + ' - ' + {task_name} + ' - ' + {lang} + ' \n' ",
          code, "\n")

    if lang == "python":
        output_file = os.path.join(
            output_dir + lang, f"{task_id}-{task_name}.py")
    else:
        output_file = os.path.join(
            output_dir + lang, f"{task_id}-{task_name}.java")

    with open(output_file, 'w') as f:
        f.write(code)



def get_code_from_response(text, language):

    if "```" not in text:
        return text.strip()

    if f"```{language}" in text:
        pattern = rf'```{language}(.*?)```'
    else:
        pattern = r'```(.*?)```'

    code_blocks = re.findall(pattern, text, re.DOTALL)

    return ''.join(code_blocks).strip()


if __name__ == "__main__":

    task_info_path = "LLM-Improved-Code-Quality/test_data/temp2/leetcode_tasks/task_info.json"

    with open(task_info_path, "r") as openfile:
        task_meta = json.load(openfile)

    output_dir = "LLM-Improved-Code-Quality/test_data/temp2/updated_code/code/"

    for task in task_meta:
        modify_code(output_dir, "python", task)
        modify_code(output_dir, "java", task)

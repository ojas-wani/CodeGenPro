import os
import re
import json
from dotenv import load_dotenv
from transformers import AutoTokenizer, LlamaForCausalLM
from groq import Groq
import requests

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY1")

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
    )

    return chat_completion.choices[0].message.content


def generate_code(output_dir, lang="python"):
    """
    Generates code from Llama for a given code task.
    """
    tasks_meta_path = r"LLM-Improved-Code-Quality/test_data/temp2/leetcode_tasks/leetcode.json"
    with open(tasks_meta_path, 'r') as f:
        tasks_meta_lists = json.load(f)

    i = 0

    for task_meta in tasks_meta_lists:
        
        if i == 200:
            break

        task_id = task_meta['id']
        task_name = task_meta['name']
        task_description = task_meta['task_description']
        template_key = f"{lang}_template"

        messages = [
            {"role": "system", "content": f"Your task is to write a {lang} program."},
            {
                "role": "user",
                "content": f"Please provide a code function implementation of the following description:\n{task_description}\n"
                f"Provide a valid {lang} code with this template:\n{task_meta[template_key]}"
            },
            {"role": "assistant", "content": f"```{lang}"}
        ]

        # response = get_llama_response(messages)
        code = get_groq_llama_response(messages)

        # code = get_code_from_response(
        #     response, lang)

        print(code)

        if lang == "python":
            output_file = os.path.join(
                output_dir + lang, f"{task_id}-{task_name}.py")
        else:
            output_file = os.path.join(
                output_dir + lang, f"{task_id}-{task_name}.java")

        with open(output_file, 'w') as f:
            f.write(code)

        i += 1


if __name__ == "__main__":
    output_directory = "LLM-Improved-Code-Quality/test_data/temp2/code/"
    generate_code(output_directory, lang="python")
    generate_code(output_directory, lang="java")

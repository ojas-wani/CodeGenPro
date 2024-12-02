import base64
import json
import os
import re
from groq import Groq  # Assuming Groq is the correct library

# Set the API key for Groq
os.environ["GROQ_API_KEY"] = "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"

# Initialize the Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def get_groq_llama_response(messages, model='llama-3.2-90b-vision-preview'):
    """
    Returns the response from the Llama model using Groq for a given prompt.
    """
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=0.0
    )
    return chat_completion.choices[0].message.content


def process_image_with_groq(image_path):
    """
    Processes an image with the Groq Llama model.
    """
    # Encode the image in base64
    base64_image = encode_image(image_path)

    # Prepare messages for the Groq Llama model
    messages = [
        {
            "role": "system", "content": "Convert the provided image into Json format. Ensure that content mentioned from the page is included. Keys are 'how many testcase passed, total testcase, wrong-answer error, input, output, and expected output.'\n"
            "Requirements:\n"
            "- Output *only* Json: Return solely the Json content without any additional explanations or comments.\n"
            "- No Delimiters: Do not use code fences or delimiters like ```json.\n"
            # "- Complete Content: Do not omit any part of the page, including headers, footers, and subtext."
         ,
        
            "role": "user", "content": [
            {"type": "text", "text": "Here is the image to be processed. Give me the content only in Json format."},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{base64_image}"}
            }
        ]
        }
    ]

    # Get response from the Llama model via Groq
    llama_response = get_groq_llama_response(messages)

    return llama_response

def encode_image(image_path: str) -> str:
    """
    Encode image to base64.

    Args:
        file_path: Path to the image file

    Returns:
        str: Base64 encoded image string
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Example usage
if __name__ == "__main__":
    image_path = "LLM-Improved-Code-Quality/test_data/groq_results/submissions/submission-errors/python/wrong_answer/test.png"

    print("Processing image with Groq...")
    groq_response = process_image_with_groq(image_path)

    print("Groq Image Analysis Response:\n", groq_response)

    # Clean the response
    cleaned_str = groq_response.strip("json\n ").replace("```", " ")
    cleaned_str = "\n".join(line.strip()
                            for line in cleaned_str.splitlines() if line.strip())
    match = re.search(r'\{(.+)\}', cleaned_str, re.DOTALL)
    json_answer = json.loads(f"{{{match.group(1)}}}")

    print("Jsonify answer\n", json_answer)

    print("Done.")

    print(json_answer['input'])
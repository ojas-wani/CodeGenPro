import base64
import json
import os
import re
from dotenv import load_dotenv
from groq import Groq  # Assuming Groq is the correct library

load_dotenv()

# Set the API key for Groq
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY2")

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
        stop="```",
        temperature=0.0,
        # top_p=1,
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
        {"role": "user", "content": [
            {
                "type": "text", 
                "text": "You are a project Manager who reviews. You got the code submission image of testing platform which contains the Error, input parameters, output, and expected output. As a manager, you analyze the image and get complete error including line number(if mentioned), input, output, and expected output to give it back to the developer.  \n"
                "Requirements:\n"
                "- Example Json: {Error:"", Input: {'parameter1': "", 'paramater2':"", ...}, expected: "", output: ""}\n"
                "Here is the image to be processed."
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{base64_image}"}
            },
        ]
        },
        {"role": "assistant", "content": "```Json"}
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
    image_path = r"LLM-Improved-Code-Quality\test_data\temp2\updated_code\submissions\code1_submission-errors\python\runtime_error\001-two-sum.png"

    print("Processing image with Groq...")
    groq_response = process_image_with_groq(image_path)

    print("Groq Image Analysis Response:\n", groq_response)

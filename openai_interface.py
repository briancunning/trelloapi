# openai_interface.py

import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI API with your key from the .env file
openai.api_key = os.getenv('OPENAI_API_KEY')


def fetch_code_from_openai(prompt_text: str) -> str:
    """
    Fetch Python code from OpenAI based on the given prompt.
    """
    print("Sending prompt to OpenAI...")

    response = openai.Completion.create(
        engine="davinci",  # Specify the GPT-4 engine
        prompt=prompt_text,
        max_tokens=150
    )

    if response and response.choices:
        print("Received response from OpenAI.")
        return response.choices[0].text.strip()
    else:
        print("Failed to get a response from OpenAI.")
        return ""


def execute_code(code: str):
    """
    Execute the given Python code.
    """
    exec(code)


def main():
    # Prompt for a user story or task
    task = input("Add two plus two and output the result.")

    # Construct the prompt for OpenAI
    prompt_text = f"Return python code only. No instructions in plain English. Write a Python function to implement the following task: {task}." \
                  f" Your response should be a complete python module that can be executed locally verbatim." \
                  f" Do not respond with anything that is not python."

    print("\nprompt_text:\n")
    print(prompt_text)

    # Fetch code from OpenAI
    code = fetch_code_from_openai(prompt_text)

    # Display the fetched code for review
    print("\nGenerated Code:\n")
    print(code)

    # Ask user for confirmation to execute
    choice = input("\nDo you want to execute the above code? (yes/no): ").lower()
    if choice == 'yes':
        execute_code(code)
    else:
        print("Code execution aborted.")


if __name__ == "__main__":
    main()

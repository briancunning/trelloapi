import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI API with your key and organization ID from the .env file
openai.api_key = os.getenv('OPENAI_API_KEY')
ORGANIZATION_ID = os.getenv('OPENAI_ORGANIZATION_ID')


def test_openai_api():
    """
    Test if the OpenAI API is working by sending a basic prompt.
    """
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt="Translate the following English text to French: 'Hello, how are you?'",
            max_tokens=50,
            organization=ORGANIZATION_ID  # Use the organization ID from the .env file
        )

        print(response)

        # Check if the response contains the expected translation
        if response and response.choices and "Bonjour" in response.choices[0].text:
            print("OpenAI API is working correctly!")
            return True
        else:
            print("OpenAI API did not return the expected response.")
            return False
    except Exception as e:
        print(f"Error while testing OpenAI API: {e}")
        return False


# Run the test
test_openai_api()


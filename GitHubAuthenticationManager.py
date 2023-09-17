import requests
import os
from dotenv import load_dotenv


class GitHubAuthenticationManager:

    def __init__(self):
        # Load environment variables
        load_dotenv()

    def getToken(self):
        # Obtain the correct API token from environment variables
        return os.getenv("GITHUB_API_TOKEN")

    def getUserName(self):
        # Read GitHub user from environment variable
        return os.getenv("GITHUB_USER")


def authenticate_via_oauth():

    auth_manager = GitHubAuthenticationManager()

    # GitHub API endpoint for the specific user
    url = f"https://api.github.com/users/{auth_manager.getUserName()}"

    # Headers for OAuth
    headers = {
        "Authorization": f"token {auth_manager.getToken()}"
    }

    # Make a GET request to the GitHub API
    response = requests.get(url, headers=headers)

    return response.status_code


if __name__ == "__main__":
    status_code = authenticate_via_oauth()
    print(f"Received status code: {status_code}")


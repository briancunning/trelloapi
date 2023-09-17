import requests
import uuid
import base64
from GitHubAuthenticationManager import GitHubAuthenticationManager

# Instantiate the GitHubAuthenticationManager
auth_manager = GitHubAuthenticationManager()

# Retrieve API token and user name
GITHUB_API_TOKEN = auth_manager.getToken()
GITHUB_USER = auth_manager.getUserName()


def create_repository():
    url = f"https://api.github.com/user/repos"
    unique_repo_name = f"new_test_repo_{uuid.uuid4().hex[:6]}"
    repo_data = {
        "name": unique_repo_name,
        "description": "A test repository",
        "private": False
    }
    headers = {
        "Authorization": f"token {GITHUB_API_TOKEN}"
    }
    response = requests.post(url, headers=headers, json=repo_data)
    return response.status_code, unique_repo_name


def delete_repository(repo_name):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}"
    headers = {
        "Authorization": f"token {GITHUB_API_TOKEN}"
    }
    response = requests.delete(url, headers=headers)
    return response.status_code


def create_issue(repo_name):
    print(f"GITHUB_USER from .env: {GITHUB_USER}")
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}/issues"
    print(f"Creating issue at URL: {url}")

    issue_data = {
        "title": "Test Issue",
        "body": "This is a test issue"
    }

    headers = {
        "Authorization": f"token {GITHUB_API_TOKEN}"
    }

    response = requests.post(url, headers=headers, json=issue_data)
    print(f"Received Status Code: {response.status_code}")
    print(f"Response Content: {response.json()}")

    return response.status_code


def add_new_file_to_repo(repo_name, file_name, file_content):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}/contents/{file_name}"

    # File content needs to be base64 encoded
    encoded_content = base64.b64encode(file_content.encode()).decode()

    payload = {
        "message": f"Adding {file_name}",
        "content": encoded_content
    }

    headers = {
        "Authorization": f"token {GITHUB_API_TOKEN}"
    }

    response = requests.put(url, headers=headers, json=payload)

    return response.status_code
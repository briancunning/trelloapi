import unittest

import GitHubRepoManager


class TestGitHubIntegration(unittest.TestCase):

    def test_integration(self):
        # Step 1: Create a new repository
        status_code, repo_name = GitHubRepoManager.create_repository()
        self.assertEqual(201, status_code)

        # Step 2: Create a new issue in the repository
        status_code = GitHubRepoManager.create_issue(repo_name)
        self.assertEqual(201, status_code)

        file_name = "testFile1.txt"
        file_content = "This is a new file."

        status_code = GitHubRepoManager.add_new_file_to_repo(repo_name, file_name, file_content)

        # Assert that the status code should be 201 (Created)
        self.assertEqual(201, status_code)

        # Step 3: Delete the repository
        status_code = GitHubRepoManager.delete_repository(repo_name)
        self.assertEqual(204, status_code)


if __name__ == "__main__":
    unittest.main()

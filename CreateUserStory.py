from TrelloAPI import *

# Constants
BOARD_NAME = "LLM Team"  # Replace with the actual board name
LIST_NAME = "To Do"

# User Story Details
user_story_name = "Password Reset Functionality"
user_story_description = (
    "As a registered user, I want to be able to reset my password via email "
    "so that I can regain access to my account if I forget my password."
)

# Create the user story card on the Trello board
response = create_card(
    board_name=BOARD_NAME,
    list_name=LIST_NAME,
    card_name=user_story_name,
    card_description=user_story_description
)

# Check if the card was created successfully
if isinstance(response, dict) and "id" in response:
    print(f"User story '{user_story_name}' has been added to the '{LIST_NAME}' list on the '{BOARD_NAME}' board.")
else:
    print(f"Failed to create the user story. Response: {response}")

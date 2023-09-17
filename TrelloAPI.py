# TrelloAPI.py

import requests
import os
import logging
from dotenv import load_dotenv

# Setting up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')
BASE_URL = "https://api.trello.com/1/"

HEADERS = {
    "Accept": "application/json"
}

def get_boards():
    endpoint = f"{BASE_URL}members/me/boards"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN
    }
    logger.debug(f"Fetching boards with endpoint: {endpoint}")
    response = requests.get(endpoint, params=params)
    return response.json()


def get_lists_for_board(board_id):
    """Fetches the lists for a given board ID."""
    endpoint = f"{BASE_URL}boards/{board_id}/lists"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN
    }
    response = requests.get(endpoint, params=params)
    return response.json()


def get_lists_for_board(board_id):
    """Fetches the lists for a given board ID."""
    endpoint = f"{BASE_URL}boards/{board_id}/lists"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# ... any other Trello API functions you might have ...

# Lookup Functions
def get_board_id_by_name(board_name):
    boards_endpoint = f"{BASE_URL}/members/me/boards?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(boards_endpoint, headers=HEADERS)
    for board in response.json():
        if board['name'] == board_name:
            return board['id']
    return None

def get_card_id_by_name(board_id, card_name):
    cards_endpoint = f"{BASE_URL}/boards/{board_id}/cards?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(cards_endpoint, headers=HEADERS)
    for card in response.json():
        if card['name'] == card_name:
            return card['id']
    return None

# Task Modification Functions
def update_card_name(board_name, card_name, new_name):
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    card_id = get_card_id_by_name(board_id, card_name)
    if not card_id:
        return "Card not found."

    endpoint = f"{BASE_URL}/cards/{card_id}?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}&name={new_name}"
    response = requests.put(endpoint, headers=HEADERS)
    return response.json()

def update_card_description(board_name, card_name, new_description):
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    card_id = get_card_id_by_name(board_id, card_name)
    if not card_id:
        return "Card not found."

    endpoint = f"{BASE_URL}/cards/{card_id}?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}&desc={new_description}"
    response = requests.put(endpoint, headers=HEADERS)
    return response.json()

def update_card_due_date(board_name, card_name, due_date):
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    card_id = get_card_id_by_name(board_id, card_name)
    if not card_id:
        return "Card not found."

    endpoint = f"{BASE_URL}/cards/{card_id}?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}&due={due_date}"
    response = requests.put(endpoint, headers=HEADERS)
    return response.json()


# Comment Function
def add_comment_to_card(board_name, card_name, comment_text):
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    card_id = get_card_id_by_name(board_id, card_name)
    if not card_id:
        return "Card not found."

    comment_endpoint = f"{BASE_URL}/cards/{card_id}/actions/comments?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}&text={comment_text}"
    response = requests.post(comment_endpoint, headers=HEADERS)

    if response.status_code == 200:
        return "Comment added successfully."
    else:
        return f"Error adding comment: {response.text}"


# Look up label
def get_label_id_by_name(board_id, label_name):
    labels_endpoint = f"{BASE_URL}/boards/{board_id}/labels?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(labels_endpoint, headers=HEADERS)
    for label in response.json():
        if label['name'] == label_name:
            return label['id']
    return None


# Add Label Function
def add_label_to_card(board_name, card_name, label_name):
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    card_id = get_card_id_by_name(board_id, card_name)
    if not card_id:
        return "Card not found."

    label_id = get_label_id_by_name(board_id, label_name)
    if not label_id:
        return "Label not found."

    label_endpoint = f"{BASE_URL}/cards/{card_id}/idLabels?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}&value={label_id}"
    response = requests.post(label_endpoint, headers=HEADERS)

    if response.status_code == 200:
        return "Label added successfully."
    else:
        return f"Error adding label: {response.text}"


def create_label(board_name, label_name, label_color):
    """
    Create a new label in a Trello board.

    Parameters:
    - board_name (str): The name of the board where the label should be created.
    - label_name (str): The name of the label to be created.
    - label_color (str): The color of the label. Valid values are 'yellow', 'purple', 'blue', 'red', 'green', 'orange', 'black', 'sky', 'pink', 'lime', or 'null' (for a transparent label).

    Returns:
    - str: A message indicating the result of the operation.
    """
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    label_endpoint = f"{BASE_URL}/labels?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}&name={label_name}&color={label_color}&idBoard={board_id}"
    response = requests.post(label_endpoint, headers=HEADERS)

    if response.status_code == 200:
        return "Label created successfully."
    else:
        return f"Error creating label: {response.text}"


def create_and_add_label(board_name, card_name, label_name, label_color):
    """
    Create a new label and add it to a specified card in a Trello board.

    Parameters:
    - board_name (str): The name of the board where the label should be created and added to the card.
    - card_name (str): The name of the card (task) to which the label should be added.
    - label_name (str): The name of the label to be created.
    - label_color (str): The color of the label. Valid values are 'yellow', 'purple', 'blue', 'red', 'green', 'orange', 'black', 'sky', 'pink', 'lime', or 'null' (for a transparent label).

    Returns:
    - str: A message indicating the result of the operation.
    """
    # Create the label
    label_creation_msg = create_label(board_name, label_name, label_color)
    if "Error" in label_creation_msg:
        return label_creation_msg

    # Add the label to the card
    add_label_msg = add_label_to_card(board_name, card_name, label_name)
    return add_label_msg


def get_card_contents(board_name, card_name):
    """
    Retrieve the entire contents of a card given its name and the board it belongs to.

    Parameters:
    - board_name (str): The name of the board where the card is located.
    - card_name (str): The name of the card whose contents are to be retrieved.

    Returns:
    - dict: A dictionary containing the card's details if found, else a message indicating the card was not found.
    """
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    card_id = get_card_id_by_name(board_id, card_name)
    if not card_id:
        return "Card not found."

    card_endpoint = f"{BASE_URL}/cards/{card_id}?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(card_endpoint, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error retrieving card contents: {response.text}"


def display_card_details(card_contents):
    """
    Display the card's details in a human-readable format.

    Parameters:
    - card_contents (dict): A dictionary containing the card's details.

    Returns:
    - str: A formatted string presenting the card's details.
    """
    if not isinstance(card_contents, dict):
        return card_contents  # This handles error messages like "Board not found" or "Card not found"

    # Extracting relevant details
    card_name = card_contents.get('name', 'N/A')
    card_desc = card_contents.get('desc', 'N/A')
    card_url = card_contents.get('url', 'N/A')
    card_labels = [label['name'] for label in card_contents.get('labels', [])]
    card_members = [member['fullName'] for member in card_contents.get('members', [])]

    # Formatting the details for display
    details = f"Card Name: {card_name}\n"
    details += f"Description: {card_desc}\n"
    details += f"URL: {card_url}\n"
    details += f"Labels: {', '.join(card_labels) if card_labels else 'No labels'}\n"
    details += f"Members: {', '.join(card_members) if card_members else 'No members assigned'}\n"

    return details


# ... previous code ...

def create_card(board_name, list_name, card_name, card_description=""):
    """Creates a card in the specified board and list."""
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    # Fetching the list ID using list name and board ID
    lists_endpoint = f"{BASE_URL}boards/{board_id}/lists?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(lists_endpoint)
    lists = response.json()
    list_id = next((lst['id'] for lst in lists if lst['name'] == list_name), None)

    if not list_id:
        return "List not found."

    # Creating the card
    card_endpoint = f"{BASE_URL}cards?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}"
    payload = {
        "name": card_name,
        "desc": card_description,
        "idList": list_id
    }
    response = requests.post(card_endpoint, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error creating card: {response.text}"


def archive_card(board_name, card_name):
    """Archives (or closes) a card in the specified board."""
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    card_id = get_card_id_by_name(board_id, card_name)
    if not card_id:
        return "Card not found."

    card_endpoint = f"{BASE_URL}cards/{card_id}?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}&closed=true"
    response = requests.put(card_endpoint)

    if response.status_code == 200:
        return "Card archived successfully."
    else:
        return f"Error archiving card: {response.text}"


def archive_all_cards(board_name):
    """Archives all cards in the specified board."""
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    cards_endpoint = f"{BASE_URL}boards/{board_id}/cards?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(cards_endpoint)
    cards = response.json()

    if not cards:
        return "No cards to archive."

    for card in cards:
        card_id = card['id']
        archive_endpoint = f"{BASE_URL}cards/{card_id}?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}&closed=true"
        requests.put(archive_endpoint)

    return "All cards archived successfully."


def move_card_to_next_list(board_name, card_name):
    """Moves a card to the next list in the workflow."""
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    card_id = get_card_id_by_name(board_id, card_name)
    if not card_id:
        return "Card not found."

    # Get the current list ID of the card
    card_endpoint = f"{BASE_URL}cards/{card_id}?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(card_endpoint)
    card_data = response.json()
    current_list_id = card_data['idList']

    # Get all lists of the board
    lists_endpoint = f"{BASE_URL}boards/{board_id}/lists?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(lists_endpoint)
    lists = response.json()

    # Find the position of the current list in the board's list sequence
    list_ids = [lst['id'] for lst in lists]
    try:
        current_list_index = list_ids.index(current_list_id)
    except ValueError:
        return "Current list of the card not found in the board."

    # If the card is already in the last list, we can't move it further
    if current_list_index == len(list_ids) - 1:
        return "Card is already in the last list."

    # Move the card to the next list in the sequence
    next_list_id = list_ids[current_list_index + 1]
    move_endpoint = f"{BASE_URL}cards/{card_id}?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}&idList={next_list_id}"
    response = requests.put(move_endpoint)

    if response.status_code == 200:
        return f"Card moved to the next list successfully."
    else:
        return f"Error moving card: {response.text}"

def set_card_to_done(board_name, card_name):
    """
    Moves a card to the "Done" list on the specified board.

    Parameters:
    - board_name (str): The name of the board where the card is located.
    - card_name (str): The name of the card to be moved.

    Returns:
    - str: A message indicating the result of the operation.
    """
    # Get the board ID
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        return "Board not found."

    # Get the card ID
    card_id = get_card_id_by_name(board_id, card_name)
    if not card_id:
        return "Card not found."

    # Get the ID of the "Done" list
    lists = get_lists_for_board(board_id)
    done_list_id = next((lst['id'] for lst in lists if lst['name'] == "Done"), None)
    if not done_list_id:
        return "Done list not found on the board."

    # Move the card to the "Done" list
    endpoint = f"{BASE_URL}cards/{card_id}?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}&idList={done_list_id}"
    response = requests.put(endpoint, headers=HEADERS)

    if response.status_code == 200:
        return "Card moved to Done successfully."
    else:
        return f"Error moving card to Done: {response.text}"

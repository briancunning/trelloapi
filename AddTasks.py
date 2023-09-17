from TrelloAPI import get_board_id_by_name, create_card


def add_tasks_to_trello(board_name, tasks):
    # Authenticate with the Trello API using stored environment variables (this is done in the TrelloAPI module)

    # Retrieve the board ID using the board's name
    board_id = get_board_id_by_name(board_name)
    if not board_id:
        print(f"Board '{board_name}' not found.")
        return

    # The list name you mentioned
    list_name = "To Do"

    # Add tasks to the 'To Do' list
    for task in tasks:
        card_name = task['name']
        card_description = task.get('description', '')  # Description is optional

        # Add a new card (ticket) to the 'To Do' list with the provided details
        response = create_card(board_name, list_name, card_name, card_description)
        if isinstance(response, dict) and 'id' in response:
            print(f"Task '{card_name}' added successfully!")
        else:
            print(f"Error adding task '{card_name}': {response}")


if __name__ == "__main__":
    BOARD_NAME = "Test Board"  # Replace with your board's name
    TASKS = [
        {'name': 'Task 1', 'description': 'Description for Task 1'},
        {'name': 'Task 2', 'description': 'Description for Task 2'},
        # ... add more tasks as needed
    ]

    add_tasks_to_trello(BOARD_NAME, TASKS)

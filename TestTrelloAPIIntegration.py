import unittest
from TrelloAPI import *


class TestTrelloAPIIntegration(unittest.TestCase):

    BOARD_NAME = "Test Board"
    CARD_NAME = "Integration Test Card"
    CARD_DESCRIPTION = "Initial description for integration test."
    UPDATED_DESCRIPTION = "Updated description after creation."
    COMMENT_TEXT = "This is a test comment for integration."
    LABEL_NAME = "Integration Test Label"
    LABEL_COLOR = "blue"

    def test_integration_flow(self):
        # 1. Archive all cards
        response = archive_all_cards(self.BOARD_NAME)
        self.assertIn(response, ["All cards archived successfully.", "No cards to archive."])

        # 2. Create a new card
        list_name = "To Do"
        card_description = "This is a test card."
        card = create_card(self.BOARD_NAME, list_name, self.CARD_NAME, card_description)
        self.assertEqual(card['name'], self.CARD_NAME)
        self.assertEqual(card['desc'], card_description)

        # 3. Add a comment to the card
        comment = "This is a test comment."
        response = add_comment_to_card(self.BOARD_NAME, self.CARD_NAME, comment)
        self.assertEqual("Comment added successfully.", response)

        # 4. Update the card description
        new_description = "Updated card description."
        updated_card = update_card_description(self.BOARD_NAME, self.CARD_NAME, new_description)
        self.assertEqual(updated_card['desc'], new_description)

        # 5. Add a new label to the card
        label_name = "Integration Test Label"
        label_color = "green"
        response = create_and_add_label(self.BOARD_NAME, self.CARD_NAME, label_name, label_color)
        self.assertEqual("Label added successfully.", response)

        # 6. Move the card to the next list in the workflow
        response = move_card_to_next_list(self.BOARD_NAME, self.CARD_NAME)
        self.assertEqual("Card moved to the next list successfully.", response)

        # 7. Set the card to "Done"
        response = set_card_to_done(self.BOARD_NAME, self.CARD_NAME)
        self.assertEqual("Card moved to Done successfully.", response)

        # 8. Archive the card
        response = archive_card(self.BOARD_NAME, self.CARD_NAME)
        self.assertEqual("Card archived successfully.", response)


if __name__ == "__main__":
    unittest.main()

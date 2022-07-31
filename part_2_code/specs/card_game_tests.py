import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):


    def setUp(self):
        self.card1 = Card("Clubs", 10)
        self.card2 = Card("Ace", 1)
        self.card_game = CardGame()

# def check_for_ace(self):
    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card2))

# def highest_card(self):
    def test_highest_card(self):
        self.assertEqual(self.card1, self.card_game.highest_card(self.card1, self.card2))

# def cards_total(self):
    def test_cards_total(self):
        cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 11", self.card_game.cards_total(cards))



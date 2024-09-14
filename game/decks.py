"""
Deck class
Build a deck of cards, shuffles the cards and deals a hand of cards.
"""
import random
from .card import Card, Suit
from .variables import RANKS


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.trump = None
        self.build()

    def build(self) -> None:
        for suit in Suit:
            for rank in RANKS:
                card = Card(rank, suit)
                self.cards.append(card)

        self.shuffle()
        self.get_trump()

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def get_trump(self) -> None:
        self.trump = self.cards[0].suit

    def deal(self, num_cards=6) -> list[Card]:
        hand = []
        for _ in range(num_cards):
            card = self.cards.pop()
            hand.append(card)
        return hand

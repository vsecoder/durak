from .card import Card

class Player:
    def __init__(self, id: int):
        self.id = id
        self.hand = []

    def add_cards(self, cards: list[Card]) -> None:
        [self.hand.append(card) for card in cards]

    def remove_card(self, card: Card) -> None:
        self.hand.remove(card)

    def get_hand(self) -> list[Card]:
        return self.hand


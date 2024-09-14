from enum import Enum


class Suit(Enum):
    CLUBS = "C"
    DIAMONDS = "D"
    HEARTS = "H"
    SPADES = "S"

    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return self.value


class Card:
    def __init__(self, rank: str, suit: Suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def __repr__(self) -> str:
        return f"{self.rank}{self.suit}"

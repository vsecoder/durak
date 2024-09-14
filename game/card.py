"""
Cards class

rank: str
suit: str
"""
class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f'{self.rank}{self.suit}'
    
    def __repr__(self) -> str:
        return f'{self.rank}{self.suit}'

from ..variables import RANKS
from ..card import Card, Suit


def is_valid_defend(attack: Card, defend: Card, trump: Suit) -> bool:
    """
    Проверяет, может ли карта защиты побить карту атаки.

    :param attack: Card, представляющая атакующую карту, например "7H" (7 червей)
    :param defend: Card, представляющая карту защиты, например "8H" (8 червей)
    :param trump: Suit, представляющая козырную масть, например "C" (трефы)
    :return: True, если карта защиты может побить карту атаки, иначе False.
    """

    # Если карты одной масти, проверяем старшинство ранга
    if attack.suit == defend.suit:
        return RANKS.index(defend.rank) > RANKS.index(attack.rank)

    # Если карта защиты - козырь, а карта атаки - не козырь
    if defend.suit == trump and attack.suit != trump:
        return True

    # В остальных случаях карта защиты не может побить карту атаки
    return False


if __name__ == "__main__":
    print(
        is_valid_defend(
            Card("7", Suit.HEARTS), 
            Card("8", Suit.HEARTS), 
            Suit.CLUBS
        )
    )  # True (одна масть, ранг выше)

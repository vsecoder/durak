from ..variables import RANKS
from ..card import Card


def is_valid_defend(atack: Card, defend: Card, trump: str) -> bool:
    """
    Проверяет, может ли карта защиты побить карту атаки.

    :param atack: Card, представляющая атакующую карту, например "7H" (7 червей)
    :param defend: Card, представляющая карту защиты, например "8H" (8 червей)
    :param trump: строка, представляющая козырную масть, например "C" (трефы)
    :return: True, если карта защиты может побить карту атаки, иначе False.
    """

    # Если карты одной масти, проверяем старшинство ранга
    if atack.suit == defend.suit:
        return RANKS.index(defend.rank) > RANKS.index(atack.rank)

    # Если карта защиты - козырь, а карта атаки - не козырь
    if defend.suit == trump and atack.suit != trump:
        return True

    # В остальных случаях карта защиты не может побить карту атаки
    return False


if __name__ == "__main__":
    print(
        is_valid_defend(Card("7", "H"), Card("8", "H"), "C")
    )  # True (одна масть, ранг выше)

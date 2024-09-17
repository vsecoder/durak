from ..card import Card, Suit


def is_valid_throw(table_cards: list[Card], card: Card):
    """
    Проверяет, можно ли подкинуть карту

    :param table_cards: list[Card], представляющая стол (массив карт)
    :param card: Card, представляющая карту, которую хотят подкинуть, например "8H" (8 червей)
    """
    return card.rank in [table_card.rank for table_card in table_cards]

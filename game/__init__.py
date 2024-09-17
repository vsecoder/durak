from .decks import Deck
from .player import Player
from .card import Card

from .logic.defend import is_valid_defend
from .logic.throw import is_valid_throw


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.current_player_index = 0
        self.attacker = None
        self.defender = None
        self.cards_on_table = []  # Карты, которые бьются
        self.pressed_cards = []   # Побитые карты

    def add_player(self, id: int) -> Player:
        if len(self.players) == 6:
            raise ValueError("Cannot add more than 6 players.")
        player = Player(id)
        self.players.append(player)
        return player

    def deal_cards(self) -> None:
        for player in self.players:
            player.add_cards(self.deck.deal(6 - len(player.hand)))

    def start_attack(self, attacker_id: int) -> None:
        self.attacker = next(
            player for player in self.players if player.id == attacker_id
        )
        self.defender = self.get_next_player(self.attacker.id)
        self.cards_on_table = []
        print(f"Player {self.attacker.id} is attacking Player {self.defender.id}.")

    def get_next_player(self, current_id: int) -> Player:
        current_index = next(
            i for i, player in enumerate(self.players) if player.id == current_id
        )
        next_index = (current_index + 1) % len(self.players)
        return self.players[next_index]

    def attack_with_card(self, card: Card) -> None:
        if self.attacker and card in self.attacker.get_hand():
            self.attacker.remove_card(card)
            self.cards_on_table.append({"card": card, "pressed_card": False})
            print(f"Player {self.attacker.id} attacked with {card}.")
        else:
            raise ValueError("Card not in hand or no attacker set.")

    def defend_with_card(self, attack_card: Card, defend_card: Card) -> None:
        if not self.attacker:
            raise ValueError("No attacker set.")

        if self.defender and defend_card in self.defender.get_hand():
            for table_card in self.cards_on_table:
                if table_card["pressed_card"] or table_card["card"] != attack_card:
                    continue
                table_card["pressed_card"] = defend_card
                self.defender.remove_card(defend_card)
                print(f"Player {self.defender.id} defended with {defend_card}.")
                break
            else:
                raise ValueError("No matching card on table to defend.")
        else:
            raise ValueError("Card not in hand or no defender set.")

    def get_table_cards(self) -> None:
        cards = []
        for table_card in self.cards_on_table:
            cards.append(table_card["card"])
            if table_card["pressed_card"]:
                cards.append(table_card["pressed_card"])

        return cards

    def take_table(self) -> None:
        if not self.attacker or not self.defender:
            raise ValueError("No attacker or defender set.")

        print(f"Player {self.defender.id} takes table cards.")

        self.defender.add_cards(self.get_table_cards())

    def end_turn(self) -> None:
        if not self.cards_on_table:
            print("No cards played this turn.")
            return

        print(f"Player {self.players[self.current_player_index].id}'s turn.")

        self.pressed_cards = self.get_table_cards()

        print(f"Pressed cards: {self.pressed_cards}")

        self.cards_on_table = []
        self.attacker = None
        self.defender = None
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

        self.deal_cards()

    def is_valid_defend(self, card_to_attack: Card, card_to_defend: Card) -> bool:
        is_valid = is_valid_defend(card_to_attack, card_to_defend, self.deck.trump)
        print(f"{card_to_attack} / {card_to_defend} is valid: {is_valid}")
        return is_valid

    def is_valid_throw(self, card: Card):
        is_valid = is_valid_throw(self.get_table_cards(), card)
        print(f"Throw is valid: {is_valid}")
        return is_valid

    def test(self):
        # Пример игрового процесса
        print("Test game started.")

        self.start_attack(self.players[0].id)  # Игрок 1 начинает атаку
        card_to_attack = self.players[0].get_hand()[0]  # Для примера берём первую карту
        self.attack_with_card(card_to_attack)

        card_to_defend = self.players[1].get_hand()[0]  # Для примера берём первую карту
        self.defend_with_card(card_to_attack, card_to_defend)

        self.is_valid_defend(card_to_attack, card_to_defend)

        # Игрок 1 продолжает атаку
        card_to_attack = self.players[0].get_hand()[0]  
        self.is_valid_throw(card_to_attack)
        self.attack_with_card(card_to_attack)

        # Игрок 2 забиращает карты со стола
        self.take_table()

        # заканчиваем ход первого игрока
        self.end_turn()

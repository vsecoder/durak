from game import Game

if __name__ == "__main__":
    game = Game()
    game.add_player(1)
    game.add_player(2)
    game.deal_cards()

    for player in game.players:
        print(f"Player {player.id} has {len(player.hand)} cards: {player.hand}")

    print(f"In decks: {len(game.deck.cards)} cards")
    print(f"Thumb: {game.deck.trump}")

    game.test()

    for player in game.players:
        print(f"Player {player.id} has {len(player.hand)} cards: {player.hand}")

    print(f"In decks: {len(game.deck.cards)} cards")

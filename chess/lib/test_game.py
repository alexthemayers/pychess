from game import Game
from player import Player


def test_rotate_players_initial_state():
    # Test that when the function is called with initial state, it toggles the value
    player1 = Player("test", "white")
    player2 = Player("test", "black")
    game = Game((player1, player2))
    assert game.current_player() is player1  # Initial state
    game.rotate_players()
    assert game.current_player() is player2  # After calling rotate_players
    game.rotate_players()
    assert game.current_player() is player1  # Back to the initial state

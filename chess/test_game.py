import uuid

from chess.active_instance import ActiveInstance
from chess.board import Board
from chess.player import Player


def test_rotate_players_initial_state():
    # Test that when the function is called with initial state, it toggles the value
    player1 = Player("test", "white")
    player2 = Player("test", "black")
    token = uuid.uuid4()
    game = ActiveInstance(Board(), token)
    game.add_player(player1)
    game.add_player(player2)
    assert game.current_player() is player1  # Initial state
    game.rotate_players()
    assert game.current_player() is player2  # After calling rotate_players
    game.rotate_players()
    assert game.current_player() is player1  # Back to the initial state

from game import Game, rotate_players


def test_singleton_instance():
    # Test that only one instance of Game is created
    game1 = Game()
    game2 = Game()
    assert game1 is game2


def test_rotate_players_initial_state():
    # Test that when the function is called with initial state, it toggles the value
    game = Game()
    assert game.second_player_turn is False  # Initial state
    rotate_players(game)
    assert game.second_player_turn is True  # After calling rotate_players
    rotate_players(game)
    assert game.second_player_turn is False  # Back to the initial state

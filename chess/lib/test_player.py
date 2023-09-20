from unittest.mock import patch

from player import get_new_player_from_cli, Player, get_current_turn


def test_get_new_player_valid_input():
    with patch('builtins.input', side_effect=["Alice", "white"]):
        player = get_new_player_from_cli()
    assert isinstance(player, Player)
    assert player.name == "Alice"
    assert player.team == "white"


def test_get_new_player_invalid_input_then_valid():
    with patch('builtins.input', side_effect=["Bob", "red", "white"]):
        player = get_new_player_from_cli()
    assert isinstance(player, Player)
    assert player.name == "Bob"
    assert player.team == "white"


def test_get_new_player_invalid_input_then_valid_with_different_team():
    with patch('builtins.input', side_effect=["Charlie", "blue", "black"]):
        player = get_new_player_from_cli()
    assert isinstance(player, Player)
    assert player.name == "Charlie"
    assert player.team == "black"


def test_get_current_turn_no_last_player():
    players = [Player("Alice", "white"), Player("Bob", "black")]
    last_player = None
    current_turn = get_current_turn(last_player, players)
    assert current_turn == players[0]


def test_get_current_turn_with_last_player():
    players = [Player("Alice", "white"), Player("Bob", "black")]
    last_player = players[0]
    current_turn = get_current_turn(last_player, players)
    assert current_turn == players[1]


def test_get_current_turn_with_last_player_at_end_of_list():
    players = [Player("Alice", "white"), Player("Bob", "black")]
    last_player = players[1]
    current_turn = get_current_turn(last_player, players)
    assert current_turn == players[0]


def test_get_current_turn_with_one_player():
    players = [Player("Alice", "white")]
    last_player = None
    current_turn = get_current_turn(last_player, players)
    assert current_turn == players[0]


def test_get_current_turn_with_empty_player_list():
    players = []
    last_player = None
    current_turn = get_current_turn(last_player, players)
    assert current_turn is None

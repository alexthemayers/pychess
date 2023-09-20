from typing import List
from unittest.mock import patch

from chess.input import (
    is_move_primitive,
    is_possible_diagonal_move,
    is_possible_horizontal_move,
    is_possible_vertical_move,
    is_possible_l_move,
    get_move,
    check_move_notation
)


def test_check_move_notation_valid():
    valid_moves = ["a1", "b2", "c3", "d4"]
    for move in valid_moves:
        assert check_move_notation(move)


def test_check_move_notation_invalid():
    invalid_moves = ["11", "bb", "3", "d", "z9", "a9", "z8"]
    for move in invalid_moves:
        assert not check_move_notation(move)


def test_is_move_primitive_valid():
    valid_moves = [("a1", "b2"), ("c3", "d4")]
    for move in valid_moves:
        assert is_move_primitive(move)


def test_is_move_primitive_invalid():
    invalid_moves = [("1a", "2b"), ("c3", "1a"), ("i1", "a"), ("a9", "b2"), ("h4", "h4")]
    for move in invalid_moves:
        assert not is_move_primitive(move)


def test_is_possible_diagonal_move_valid():
    valid_moves = [("a1", "b2"), ("a1", "c3"), ("c3", "d4"), ("h8", "g7")]
    for move in valid_moves:
        assert is_possible_diagonal_move(move)


def test_is_possible_diagonal_move_invalid():
    invalid_moves = [("a1", "c4"), ("c3", "f5"), ("h8", "d1")]
    for move in invalid_moves:
        assert not is_possible_diagonal_move(move)


def test_is_possible_horizontal_move_valid():
    valid_moves = [("a1", "b1"), ("c3", "d3"), ("h8", "g8")]
    for move in valid_moves:
        assert is_possible_horizontal_move(move)


def test_is_possible_horizontal_move_invalid():
    invalid_moves = [("a2", "c1"), ("c2", "e3"), ("h2", "a8")]
    for move in invalid_moves:
        assert not is_possible_horizontal_move(move)


def test_is_possible_vertical_move_valid():
    valid_moves = [("a1", "a3"), ("e8", "e3"), ("a1", "a8")]
    for move in valid_moves:
        assert is_possible_vertical_move(move)


def test_is_possible_vertical_move_invalid():
    invalid_moves = [("a1", "b3"), ("c3", "d3"), ("a8", "h1")]
    for move in invalid_moves:
        assert not is_possible_vertical_move(move)


def test_is_possible_l_move_valid():
    valid_moves = [("a1", "b3"), ("c3", "d1"), ("h8", "g6")]
    for move in valid_moves:
        assert is_possible_l_move(move)


def test_is_possible_l_move_invalid():
    invalid_moves = [("a1", "a3"), ("a5", "c5"), ("f3", "h1"), ("g2", "h1"), ("a8", "h1")]
    for move in invalid_moves:
        assert not is_possible_l_move(move)


def test_get_move():
    test_inputs: List[List[str, str]] = [["a1", "a2"],
                                         [["a1", "a3"], ["a5", "c5"], ["f3", "h1"], ["g2", "h1"], ["a8", "h1"]]]
    for test_input in test_inputs:
        with patch('builtins.input', side_effect=test_input):
            move = get_move()
        assert move == (test_input[0], test_input[1])

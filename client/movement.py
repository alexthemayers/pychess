from typing import Tuple

from input import (
    is_possible_diagonal_move,
    is_possible_vertical_move,
    is_possible_horizontal_move,
    is_possible_l_move,
    is_move_primitive
)
from mapping import (
    calculate_vertical_difference,
    calculate_diagonal_difference,
    calculate_horizontal_difference,
    calculate_xy_difference
)


def knight_can_make(move: Tuple[str, str]) -> bool:
    if not is_move_primitive(move):
        return False
    if move[0] == move[1]:
        return False
    return is_possible_l_move(move)


def bishop_can_make(move: Tuple[str, str]) -> bool:
    if not is_move_primitive(move):
        return False
    if move[0] == move[1]:
        return False
    return is_possible_diagonal_move(move)


def king_can_make(move: Tuple[str, str]) -> bool:
    if not is_move_primitive(move):
        return False
    if move[0] == move[1]:
        return False
    if is_possible_vertical_move(move):
        if close_enough_for_king(move):
            return True
    if is_possible_horizontal_move(move):
        if close_enough_for_king(move):
            return True
    if is_possible_diagonal_move(move):
        if close_enough_for_king(move):
            return True
    return False


def rook_can_make(move: Tuple[str, str]) -> bool:
    if not is_move_primitive(move):
        return False
    if move[0] == move[1]:
        return False
    if is_possible_horizontal_move(move):
        return True
    if is_possible_vertical_move(move):
        return True
    return False


def queen_can_make(move: Tuple[str, str]) -> bool:
    if not is_move_primitive(move):
        return False
    if move[0] == move[1]:
        return False
    if is_possible_horizontal_move(move):
        return True
    if is_possible_vertical_move(move):
        return True
    if is_possible_diagonal_move(move):
        return True
    return False


def pawn_can_make(move: Tuple[str, str], has_moved: bool, team: str) -> bool:
    if not is_move_primitive(move):
        return False
    if move[0] == move[1]:
        return False
    before = move[0]
    after = move[1]
    horizontal_difference = calculate_horizontal_difference(before, after)
    vertical_difference = calculate_vertical_difference(before, after)
    if not has_moved:
        # first move, two paces
        if team == "white":
            if horizontal_difference == 0 and 1 <= vertical_difference <= 2:
                return True
        if team == "black":
            if horizontal_difference == 0 and -2 <= vertical_difference <= -1:
                return True


def close_enough_for_king(move: Tuple[str, str]) -> bool:
    horizontal_difference, vertical_difference = calculate_xy_difference(move)
    if vertical_difference == 1 or vertical_difference == -1 and horizontal_difference == 1 or horizontal_difference == -1:
        return True
    # left, right
    if vertical_difference == 0 and horizontal_difference == 1 or horizontal_difference == -1:
        return True
    # up, down
    if vertical_difference == 1 or vertical_difference == -1 and horizontal_difference == 0:
        return True
    diagonal_difference = calculate_diagonal_difference(move[0], move[1])
    if diagonal_difference == 1 or diagonal_difference == -1:
        return True
    return False

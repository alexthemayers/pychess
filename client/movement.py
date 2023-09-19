from typing import Tuple

from input import (
    is_possible_diagonal_move,
    is_possible_vertical_move,
    is_possible_horizontal_move,
    is_possible_l_move,
    is_move_primitive
)
from mapping import (
    calculate_diagonal_difference,
    calculate_xy_difference
)


def knight_can_make(move: Tuple[str, str]) -> bool:
    """
    returns a boolean indicating whether a knight could make the provided move. this does not check if another piece is
    blocking this move.
    :param move:
    :return:
    """
    if not is_move_primitive(move):
        return False
    if move[0] == move[1]:
        return False
    return is_possible_l_move(move)


def bishop_can_make(move: Tuple[str, str]) -> bool:
    """
    returns a boolean indicating whether a bishop could make the provided move. this does not check if another piece is
    blocking this move.
    :param move:
    :return:
    """
    if not is_move_primitive(move):
        return False
    if move[0] == move[1]:
        return False
    return is_possible_diagonal_move(move)


def king_can_make(move: Tuple[str, str]) -> bool:
    """
    returns a boolean indicating whether a king could make the provided move. this does not check if another piece is
    blocking this move.
    :param move:
    :return:
    """
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
    """
    returns a boolean indicating whether a rook could make the provided move. this does not check if another piece is
    blocking this move.
    :param move:
    :return:
    """
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
    """
    returns a boolean indicating whether a queen could make the provided move. this does not check if another piece is
    blocking this move.
    :param move:
    :return:
    """
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
    """
    returns a boolean indicating whether a pawn could make the provided move, this does not check if another piece is
    blocking this move
    :param move:
    :param has_moved:
    :param team:
    :return:
    """
    if not is_move_primitive(move):
        return False
    if move[0] == move[1]:
        return False
    horizontal_difference, vertical_difference = calculate_xy_difference(move)
    going_straight = horizontal_difference == 0
    going_diagonal = horizontal_difference == -1 or horizontal_difference == 1
    if has_moved:
        # first move, two paces
        if going_straight or going_diagonal:
            if team == "white":
                if vertical_difference == 1:
                    return True
            if team == "black":
                if vertical_difference == -1:
                    return True
        return False

    if not has_moved:
        # first move, two paces
        if going_straight:
            if team == "white":
                if 1 <= vertical_difference <= 2:
                    return True
            if team == "black":
                if -2 <= vertical_difference <= -1:
                    return True
        if going_diagonal:
            if team == "white":
                if vertical_difference == 1:
                    return True
            if team == "black":
                if vertical_difference == -1:
                    return True
            return False
    return False


def close_enough_for_king(move: Tuple[str, str]) -> bool:
    """
    returns a boolean indicating whether the provided move is within the expected range of a king
    :param move:
    :return:
    """
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

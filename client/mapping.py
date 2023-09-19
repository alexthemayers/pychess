from typing import Tuple

_Y_KEY = 1
_X_KEY = 0


def calculate_diagonal_difference(before: str, after: str) -> int:
    """
    returns the diagonal difference between two points specified as a move primitive in cases where we have a perfect
    diagonal: vertical difference == horizontal difference
    :param before:
    :param after:
    :return:
    """
    # FIXME This is more nuanced than this, cater for positive and negative return values properly
    return calculate_vertical_difference(before, after)


def calculate_vertical_difference(before: str, after: str) -> int:
    """
    returns the vertical difference between two points specified as a move primitive
    :param before:
    :param after:
    :return:
    """
    ret = int(after[_Y_KEY]) - int(before[_Y_KEY])
    return ret


def calculate_horizontal_difference(before: str, after: str) -> int:
    """
    returns the horizontal difference between two points specified as a move primitive
    :param before:
    :param after:
    :return:
    """
    ret = ord(after[_X_KEY]) - ord(before[_X_KEY])
    return ret


def calculate_xy_difference(move: Tuple[str, str]) -> Tuple[int, int]:
    """
    returns the horizontal and vertical difference between two points specified as a move primitive
    :param move:
    :return:
    """
    before = move[0]
    after = move[1]
    horizontal_difference = calculate_horizontal_difference(before, after)
    vertical_diff = calculate_vertical_difference(before, after)
    return horizontal_difference, vertical_diff

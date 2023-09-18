from typing import Tuple

_Y_KEY = 1
_X_KEY = 0


def calculate_diagonal_difference(before: str, after: str) -> int:
    # FIXME This is more nuanced than this, cater for positive and negative return values properly
    return calculate_vertical_difference(before, after)


def calculate_vertical_difference(before: str, after: str) -> int:
    ret = int(after[_Y_KEY]) - int(before[_Y_KEY])
    return ret


def calculate_horizontal_difference(before: str, after: str) -> int:
    ret = ord(after[_X_KEY]) - ord(before[_X_KEY])
    return ret


def calculate_xy_difference(move: Tuple[str, str]) -> Tuple[int, int]:
    before = move[0]
    after = move[1]
    horizontal_difference = calculate_horizontal_difference(before, after)
    vertical_diff = calculate_vertical_difference(before, after)
    return horizontal_difference, vertical_diff

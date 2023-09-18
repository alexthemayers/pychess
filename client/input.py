from typing import Tuple

from mapping import calculate_vertical_difference, calculate_horizontal_difference

_Y_KEY = 0
_X_KEY = 1


def is_move_primitive(move: Tuple[str, str]) -> bool:
    for s in move:
        letter = s[0]
        number = s[1]
        if not letter.isalpha():
            return False
        if not number.isnumeric():
            return False
        if ord(letter) > ord("h") or ord(letter) < ord("a"):
            return False
        if int(number) > 8 or int(number) < 1:
            return False
    return True


def is_possible_diagonal_move(move: Tuple[str, str]):
    before = move[0]
    after = move[1]
    vertical_difference = calculate_vertical_difference(before, after)
    horizontal_difference = calculate_horizontal_difference(before, after)
    return horizontal_difference == vertical_difference


def is_possible_horizontal_move(move: Tuple[str, str]) -> bool:
    before = move[0]
    after = move[1]
    return int(before[_X_KEY]) == int(after[_X_KEY])


def is_possible_vertical_move(move: Tuple[str, str]) -> bool:
    before = move[0]
    after = move[1]
    return before[_Y_KEY] == after[_Y_KEY]


def is_possible_l_move(move: Tuple[str, str]) -> bool:
    before = move[0]
    after = move[1]
    vertical_difference = calculate_vertical_difference(before, after)
    horizontal_difference = calculate_horizontal_difference(before, after)
    if vertical_difference == 2 or vertical_difference == -2:
        if horizontal_difference == 1 or horizontal_difference == -1:
            return True
    if horizontal_difference == 2 or horizontal_difference == -2:
        if vertical_difference == 1 or vertical_difference == -1:
            return True
    return False


def get_move() -> Tuple[str, str]:
    """
    prints player prompting to screen, get's current players move input, then returns it
    :return from_coordinate, to_coordinate:
    """
    from_coordinate: str = input("Enter the coordinate of the block containing the piece you would like to move: ")
    to_coordinate: str = input("Enter the coordinate of the block that you would like to move that piece to: ")
    return from_coordinate, to_coordinate

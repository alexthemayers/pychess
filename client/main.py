#!/usr/bin/env python3

from typing import Optional, Tuple

from board import Board, move_is_possible, populate_board
from input import get_move, is_move_primitive
from player import Player, get_new_player, get_current_turn


def main():
    won: bool = False
    p1 = get_new_player()
    print("Next player:")
    p2 = get_new_player()
    # game = Game()
    board = populate_board(Board(), [p1, p2])
    current_player: Optional[Player] = None

    while not won:  # check if game over
        # print board
        print(board)

        # who's turn is it?
        current_player = get_current_turn(current_player, [p1, p2])

        # what's their move?
        print(f"It's {current_player.name}'s turn!")
        move = get_move()

        # is that move valid? is there a piece already there?
        # FIXME board.get_piece(move[0]) should not be a dependency here
        while (not player_owns_piece(board, current_player.team, move)
               and not move_is_possible(board.get_piece(move[0]), board, move)
               and not causes_check()):
            print(f"{move} is invalid")
            move = get_move()

        # make the move on the board
        board.move(move)

        """
        is it a check? 
        is it a checkmate?
        """

        # difference/move is illegal (not sure if this is the correct way forward here)
    """
    has the game been won?
    """


def player_owns_piece(board: Board, owner_team: str, move: Tuple[str, str]) -> bool:
    if not is_move_primitive(move):
        return False
    start = move[0]
    if board.get_piece(start).player.team == owner_team:
        return True
    return False


def causes_check():
    # TODO Implement me
    return False


if __name__ == "__main__":
    main()

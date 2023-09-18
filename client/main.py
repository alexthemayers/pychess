#!/usr/bin/env python3

from typing import Optional, Dict, List, Tuple

from block import _Block
from board import Board, move_is_possible
from game import Game
from input import get_move, is_move_primitive
from piece import Rook, Knight, Bishop, Queen, King
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


# TODO check out how this compromises the dependency heirarchy and find new home if necessary
def populate_board(board: Board, players: List[Player]) -> Board:
    players: Dict[str, Player] = {p.team: p for p in players}

    def __place_pawn_piece(b: _Block, team: str) -> None:
        assert str(b.position).endswith("7") or str(b.position).endswith(
            "2"), "Pawn pieces should not be placed on rows other than 7 or 2"
        b.set_piece(Rook(players[team]))

    def __place_non_pawn_piece(b: _Block, team: str) -> None:
        assert b.position.endswith("8") or b.position.endswith(
            "1"), "Non-pawn pieces should not be placed on rows other than 8 or 1"
        if b.position.startswith(("a", "h")):  # R
            b.set_piece(Rook(players[team]))
        elif b.position.startswith(("b", "g")):  # N
            b.set_piece(Knight(players[team]))
        elif b.position.startswith(("c", "f")):  # B
            b.set_piece(Bishop(players[team]))
        elif b.position.startswith("d"):  # Q
            b.set_piece(Queen(players[team]))
        elif b.position.startswith("e"):  # K
            b.set_piece(King(players[team]))
        else:
            print(f"point {b.position} should not be present on board")

    for block in board.get_board():
        if block.position.endswith("8"):
            __place_non_pawn_piece(block, "black")
        elif block.position.endswith("7"):
            __place_pawn_piece(block, "black")
        elif block.position.endswith("2"):
            __place_pawn_piece(block, "white")
        elif block.position.endswith("1"):
            __place_non_pawn_piece(block, "white")
        else:
            print(f"invalid point {block.position} present in board")
            exit(1)
        return board
    else:
        pass


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

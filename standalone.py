from typing import Optional
import os

from chess import (
    Board,
    populate_board,
    move_is_possible,
    Player,
    get_new_player_from_cli,
    get_current_turn,
    get_move
)


def run():
    os.system("clear")
    won: bool = False
    p1 = get_new_player_from_cli()
    os.system("clear")
    print("Next player:")
    p2 = get_new_player_from_cli()
    # game = Game()
    board = populate_board(Board(), [p1, p2])
    current_player: Optional[Player] = None

    while not won:  # check if game over
        os.system("clear")
        # print board
        print(board)

        # who's turn is it?
        current_player = get_current_turn(current_player, [p1, p2])

        # what's their move?
        print(f"It's {current_player.name}'s turn!")
        move = get_move()

        # is that move valid? is there a piece already there?
        piece_to_move = board.get_piece(move[0])
        current_player_owns_piece = piece_to_move.get_team() == current_player.team
        while (not current_player_owns_piece
               and not move_is_possible(piece_to_move, board, move)
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


def causes_check():
    # TODO Implement me
    return False

from Player import *
from Board import *


class Game:
    started: bool = False
    won: bool = False


    @classmethod
    def start(cls):
        PlayerHelper.init('text')
        while not Game.won:  # check if game over
            # rotate active player
            if Game.started:  # skips rotation on first turn
                PlayerHelper.rotate_players()
            if not Game.started:
                Game.started = True

            # print board
                # possibility of TUI interface for printing and text input (ncurses)
            print(BoardHelper.printable_board("text", PlayerHelper.current_player))

            # save snapshot of current board to file for recallable reference
            BoardHelper.last_board = BoardHelper.cache_board()  # TODO write a test for this

            # wait for input
            # cli input - receive text input in formal chess notation (tokenizer and parser needed for this notation)
            # mouse input - to be done once gui is established
            # update snapshot with move applied and save to memory as "Board.current_board: list[BoardPoint]"
            # compare before and after state of board and reject and roll back "after" state if 
            # difference/move is illegal (not sure if this is the correct way forward here)

            print("Game.start() has not been implemented yet!")
            # game loop goes here


if __name__ == "__main__":
    print("run main.py")
    exit(1)

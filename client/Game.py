from Player import *

class Game:
    @staticmethod
    def won(self) -> bool:
        return False

    @staticmethod
    def start(self, players: list[Player]):
        while not Game.won(): # check if game over
            # rotate active player 
            # print board 
                # print board with rotation for proper player viewing perspective
                # possibility of TUI interface for printing and text input (ncurses)
            # save snapshot of current board to file for recallable reference
            # wait for input 
                # cli input - receive text input in formal chess notation (tokenizer and parser needed for this notation)
                # mouse input - to be done once gui is established 
            # update snapshot with move applied and save to memory as "Board.current_board: list[BoardPoint]"
            # compare before and after state of board and reject and roll back "after" state if difference/move is illegal (not sure if this is the correct way forward here)

            pass
            # game loop goes here


if __name__ == "__main__":
    print("run main.py")
    exit(1)

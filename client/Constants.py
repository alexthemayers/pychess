from enum import Enum


BOARD_WIDTH = 8
BOARD_HEIGHT = 8

class Pieces(Enum):
    KING = 0
    QUEEN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    PAWN = 5

if __name__ == "__main__":
    print("run main.py")
    exit(1)
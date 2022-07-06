from Player import *


class Piece:  # superclass for all pieces instantiated later in this file
    def __init__(self, piece_type: str, player: Player):
        self.type = piece_type
        self.player = player

    def __repr__(self) -> str:
        return f"{str(self.type)} \n"


class Rook(Piece):

    def __init__(self, player):
        super().__init__("ROOK", player)
        super("ROOK", player)

    def __repr__(self) -> str:
        return super.__repr__(self)


if __name__ == "__main__":
    print("run main.py")
    exit(1)

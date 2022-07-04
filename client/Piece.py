from Piece import *
from Constants import *

class Piece(): # superclass for all pieces instantiated later in this file
    def __init__(self, type: Pieces, player: Player):
        self.name = name
    
    def isPiece(self):
        return f"i am a {self.name} \n"

class Rook(Piece):
    
    def __init__(self): 
        self.type = ROOK
    
    def isPiece(self):
        return "I am a rook"
    
r = Piece("rook")

print(r.isPiece())



if __name__ == "__main__":
    print("run main.py")
    exit(1)
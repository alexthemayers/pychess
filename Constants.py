BOARD_WIDTH = 8
BOARD_HEIGHT = 8

class Piece():
    
    
    def __init__(self, name):
        self.name = name
    
    def isPiece(self):
        return f"i am a {self.name} \n"

class Rook(Piece):
    
    def __init__(self): 
        pass
    
    def isPiece(self):
        return "I am a rook"
    
r = Piece("rook")

print(r.isPiece())


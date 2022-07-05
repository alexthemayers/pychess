from Constants import *

blockNames: list = ["this", "is"] # reversed in order to make readable entry possible alongside stack-pop logic implemented in constructor

class BoardHelper():
    def __init__(self) -> None:
        self.board = self.Board()
        
            
    class Board(): 
        class BoardPoint(): # similar to creating a struct in another language. This is just a container to house multiple related elements in a convenient way 
            def __init__(self, x: int, y: int, name: str) -> None:
                self.x = x
                self.y = y
                self.name = name
                
            def __repr__(self) -> str:
                return self.name
            
        def __init__(self) -> None:
            # self.points = [self.BoardPoint(x, y, name) for (x, name) in zip(range(1, BOARD_WIDTH + 1), blockNames) for y in range(1, BOARD_HEIGHT + 1)]
            self.points: list = []
            while len(blockNames) > 0:
                for y in range(1, BOARD_HEIGHT + 1):
                    for x in range(1, BOARD_WIDTH + 1):
                        self.points.append(self.BoardPoint(x, y, blockNames.pop()))
                        # print(self)
                        # print(len(blockNames))
        
        def __repr__(self) -> str:
            return "\t".join([str(point) for point in self.points])
    
    def printBoard(self, outType: str):
        if outType == "cli":
            print(self.board)
        elif outType == "gui":
            pass
        else: 
            print('invalid outType\ncould not print\ncheck your code, yo')
    
    
    
    
if __name__ == "__main__":
    print("run main.py")
    exit(1)
    # b = BoardHelper()
    # b.printBoard("cli")
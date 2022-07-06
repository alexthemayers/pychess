from Constants import *

blockNames: list = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
                    "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                    "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
                    "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
                    "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
                    "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
                    "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                    "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
                    ]
list.reverse(blockNames)  # reversed in order to make readable entry possible alongside stack-pop logic implemented in constructor


class BoardHelper:
    def __init__(self) -> None:
        self.board = self.Board()

    class Board:
        class BoardPoint:  # similar to creating a struct in another language. This is just a container to house multiple related elements in a convenient way 
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
                for y in reversed(range(1, BOARD_HEIGHT + 1)):
                    for x in range(1, BOARD_WIDTH + 1):
                        self.points.append(self.BoardPoint(x, y, blockNames.pop()))
                        # print(self)
                        # print(len(blockNames))

        def __repr__(self) -> str:
            ret: str = ""
            points: list[BoardHelper.Board.BoardPoint] = [point for point in self.points]
            points.reverse()
            while len(points) > 0:
                if (len(points) - 1) % 8 != 0:
                    p = points.pop()
                    ret += p.name + f"({p.x},{p.y})" + "\t"
                else:
                    p = points.pop()
                    ret += p.name + f"({p.x},{p.y})" + "\n\n"
            return ret

    def printable_board(self, out_type: str):
        if out_type.lower() == "text":
            return self.board
        elif out_type.lower() == "gui":
            pass
        elif out_type.lower() == "tui":
            pass
        else:
            print('invalid out_type\ncould not print\ncheck your code, yo')


if __name__ == "__main__":
    print("run main.py")
    exit(1)
    # b = BoardHelper()
    # print(b.printable_board("text"))

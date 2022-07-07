import json
import os
from typing import Dict, Optional
from Player import *
from json import dumps, loads
from Constants import *

blockNames: List[str] = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
                         "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                         "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
                         "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
                         "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
                         "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
                         "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                         "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
                         ]
list.reverse(blockNames)  # reversed in order to make readable entry possible alongside stack-pop logic implemented in constructor


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
        self.points: List[Board.BoardPoint] = []
        while len(blockNames) > 0:
            for y in reversed(range(1, BOARD_HEIGHT + 1)):
                for x in range(1, BOARD_WIDTH + 1):
                    self.points.append(self.BoardPoint(x, y, blockNames.pop()))
                    # print(self)
                    # print(len(blockNames))

    def __repr__(self) -> str:
        ret: str = ""
        points: List[Board.BoardPoint] = [point for point in self.points]
        points.reverse()
        while len(points) > 0:
            if (len(points) - 1) % 8 != 0:
                p = points.pop()
                ret += p.name + f"({p.x},{p.y})" + "\t"
            else:
                p = points.pop()
                ret += p.name + f"({p.x},{p.y})" + "\n\n"
        return ret


class BoardHelper:
    board = Board()
    last_board: str = None
    cache_list: Optional[Dict[int, str]] = None

    @classmethod
    def printable_board(cls, out_type: str, player: Player) -> None:
        if player.team == "black":
            pass
            # cls.rotate_board(cls.board)
        if out_type.lower() == "text":
            print(cls.board)  # magic methods at work - __repr__
        elif out_type.lower() == "gui":
            # command called to update gui board
            pass
        elif out_type.lower() == "tui":
            # command called to update tui board
            pass
        else:
            print('invalid out_type\ncould not print\ncheck your code, yo')

    @classmethod
    def rotate_board(cls, b: Board) -> None:
        print('rotate_board() is not implemented yet!')  # TODO logic to rotate board for black player perspective before rendering
        exit(1)

    @classmethod
    def cache_board(cls) -> str:
        if cls.cache_list is None:
            cls.write_cache(BOARD_CACHE)
            return BOARD_CACHE
        else:
            filename = str(len(cls.cache_list)).join(BOARD_CACHE.split("0000"))
            cls.write_cache(filename)
            return filename
    @classmethod
    def clean_cache(cls, path: str) -> bool:
        cache_limit = None
        del_me: List[str] = []
        if path in cls.cache_list.values():
            for k, v in cls.cache_list.items():
                while v != path:
                    continue
                cache_limit = k
                break

            assert (issubclass(cache_limit, int)), f"clean cache function failure. cache_limit should contain an integer, not {type(cache_limit)}"
            cls.cache_list = {key: value if key <= cache_limit else del_me.append(value) for key, value in cls.cache_list.items()}
            # should recreate cache_list retaining only values that were generated up to the most recent cache point
            for file in del_me:
                os.unlink(file)
            return True
        else:
            print("could not find filename in cache list")
            return False


    @classmethod
    def write_cache(cls, path: str) -> None:
        with open(path, "a") as f:
            if f.write(dumps(cls.board)) > 0:
                cls.cache_list[len(cls.cache_list)] = str(BOARD_CACHE)
                f.close()
            else:
                print("could not cache board! exiting!")
                f.close()
                exit(1)

    @classmethod
    def read_cache(cls, path: str) -> Board:
        with open(path, "r") as f:
            if f is not None:
                b: Board = loads(f.read())
                f.close()
                cls.clean_cache(path)
                return b
            else:
                print("could not read cache! exiting!")
                exit(1)


if __name__ == "__main__":
    print("run main.py")
    exit(1)
    # b = BoardHelper()
    # print(b.printable_board("text"))

from enum import Enum

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
BOARD_CACHE = 'board_cache0000.json'


class Team(Enum):
    TEAM_WHITE = 0
    TEAM_BLACK = 1

    def __repr__(self) -> str:
        if self.TEAM_WHITE:
            return "white"
        if self.TEAM_BLACK:
            return "black"


if __name__ == "__main__":
    print("run main.py")
    exit(1)

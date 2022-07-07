import random
from typing import List


class Player:
    def __init__(self, name: str, team: str) -> None:
        if team.lower() == "white" or "black":
            self.team = team.lower()
        else:
            print("invalid side selected")
            exit(1)
        self.name = name
        PlayerHelper.players.append(self)

    def __repr__(self) -> str:
        return f"{self.name}\t=>\t{self.team}"


class PlayerHelper:
    players: List[Player] = []
    current_player: Player = None

    @classmethod
    def init(cls, method) -> List[Player]:
        p1 = cls.get_new_player(method)
        cls.players.append(p1)
        print(f"{p1.name} joined {p1.team}!")
        p2 = cls.get_new_player(method)
        cls.players.append(p2)
        print(f"{p2.name} joined {p2.team}!")
        return cls.players

    @classmethod
    def get_new_player(cls, method) -> Player:
        options: List[str] = ["white", "black"]
        if method == 'text':
            name: str = input('Please enter your name: ').strip()
            team: str = input('Please enter your team: ').strip()
            print(f"you entered {team}")
            # with open('testfile.txt', 'w') as f:
            #     f.write("white")
            #     f.write("white")
            #     f.write("\n")
            #     f.write(team)
            #     f.write(team)
            #     f.close()
            if str(team.lower()) not in options:
                print("please choose \'white\' or \'black\'")
                p = cls.get_new_player(method)
            else:
                p = Player(name, team.lower())
            return p

    @classmethod
    def random_starter(cls) -> Player:
        assert len(cls.players) == 2, "Need 2 players to start a game in chess!"
        assert (cls.current_player is None), "Current player can't be set before a starting player is chosen!"
        random.shuffle(cls.players)
        return cls.players[0]

    @classmethod
    def rotate_players(cls) -> None:
        cls.players.reverse()


if __name__ == "__main__":
    print("run main.py")
    exit(1)

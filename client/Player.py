import random


class Player:
    def __init__(self, name: str, side: str) -> None:
        if side.lower() == "white" or "black":
            self.side = side.lower()
        else:
            print("invalid side selected")
            exit(1)
        self.name = name
        PlayerHelper.players.append(self)

    def __repr__(self) -> str:
        return f"{self.name}\t=>\t{self.side}"


class PlayerHelper:
    players: list[Player] = []

    @staticmethod
    def random_starter() -> Player:
        assert len(PlayerHelper.players) == 2, "Need 2 players to start a game in chess!"
        return random.choice(PlayerHelper.players)


if __name__ == "__main__":
    # print("run main.py")
    # exit(1)
    print(f"Random choice of available players: {PlayerHelper.random_starter()}")

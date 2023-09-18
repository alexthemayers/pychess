from typing import Optional, List


class Player:
    team: str
    name: str

    def __init__(self, name: str, team: str) -> None:
        self.team = team.lower()
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name}\t=>\t{self.team}"


def get_current_turn(last_player: Optional[Player], players: List[Player]) -> Player:
    """
    returns the first player if the last player is None, or returns the next player if not
    :param last_player:
    :param players:
    :return:
    """
    if last_player is None:
        for p in players:
            if p.team.lower() == "white":
                return p
    for p in players:
        if p is not last_player:
            return p


def get_new_player() -> Player:
    options: List[str] = ["white", "black"]
    name: str = input('Please enter your name: ').strip()
    team: str = ""
    while str(team.lower()) not in options:
        print("Please choose \'white\' or \'black\'")
        team = input('Please enter your team: ').strip()
    print(f"You entered the {team.lower()} team")
    print()
    return Player(name, team)

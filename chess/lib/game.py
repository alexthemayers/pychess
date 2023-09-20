from typing import Tuple, Optional

from board import Board
from player import Player


class Game:
    """
        Don't get too excited. We don't want this to replace the main.
        Be very intentional about what lives in here and what lives in {client,server,standalone}.py
    """
    _players: Tuple[Player, Player]
    _current_player: Player

    def __init__(self, players: Tuple[Player, Player]):
        self._players = players
        for p in players:
            if p.team == "white":
                self._current_player = p

    def rotate_players(self):
        """
        rotates players attached to a game instance
        :param game:
        :return:
        """
        for p in self._players:
            if p != self._current_player:
                self._current_player = p
                return

    def current_player(self) -> Player:
        return self._current_player

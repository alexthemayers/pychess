from typing import Optional, List
from uuid import UUID

from board import Board
from player import Player


class ActiveInstance:
    __winner = Optional[Player]

    def __init__(self, board: Board, token: UUID):
        self.__winner = None
        self._players = []
        self.__waiting_for_players = True
        self.__board = board
        self.__token = token

    __board: Board

    def board(self) -> Board:
        return self.__board

    __token: UUID

    def token(self) -> UUID:
        return self.__token

    ## PLAYERS
    _players: List[Player]
    _current_player: Player

    def players(self) -> List[Player]:
        return self._players

    def winner(self) -> (Optional[Player]):
        return self.__winner

    def add_player(self, player: Player):
        self._players.append(player)
        ## todo guard against two players on the same team
        if player.team == "white":
            self._current_player = player

    def current_player(self) -> Player:
        return self._current_player

    def rotate_players(self):
        """
        rotates players attached to a game instance
        :return:
        """
        for p in self._players:
            if p != self._current_player:
                self._current_player = p
                return

    def is_waiting_for_players(self) -> bool:
        """
        returns true if two players have not yet been added to an active game instance
        :return:
        """
        return 0 < len(self._players) < 2

    ##

    def json_state(self) -> dict[str, str | Player | None]:
        # TODO extra state should be included here: winner, check, next turn, possibly more
        return {"board": self.board().to_json(), "winner": self.winner(), "next_turn": self.current_player().team}

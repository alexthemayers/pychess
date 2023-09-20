from typing import Optional, List

from game import Game
from board import Board
from uuid import UUID
from player import Player


class ActiveInstance:
    __winner = Optional[Player]
    __waiting_for_players: bool
    __first_to_arrive = Optional[Player]
    _game: Game
    _board: Board
    _token: UUID

    def __init__(self, game: Game, board: Board, token: UUID):
        self.__won = False
        self.__waiting_for_players = True
        self._board = board
        self._token = token

    def add_player(self, player: Player):
        """
        adds players to the active instance and creates a chess game object once both players have arrived.
        TODO this feels suboptimal
        :param player:
        :return:
        """
        if self.__first_to_arrive is not None:
            self._game = Game(self.__first_to_arrive, player)
            self.__waiting_for_players = False

    def is_waiting(self) -> bool:
        return self.__waiting_for_second_player

    def token(self) -> UUID:
        return self._token

    def winner(self) -> (Optional[Player]):
        return self.__winner

    def json_state(self) -> str:
        # TODO extra state should be included here: winner, check, next turn, possibly more
        return self._board.to_json()

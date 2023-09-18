from board import Board
from player import Player


class Game:
    """
        This is a singleton class to house basic game logic.
        Don't get too excited. We don't want this to replace the main.
        Be very intentional about what lives in here and what lives in main.py
    """
    _instance = None
    second_player_turn: bool = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Game, cls).__new__(cls)
        return cls._instance

    def _play(self, player: Player, board: Board):
        """
        Turn for turn logic lives in this inner method.
        Handle the interactions the player has with the board in this method.
        :param player:
        :return:
        """
        pass


def rotate_players(game: Game):
    if game.second_player_turn:
        game.second_player_turn = False
    else:
        game.second_player_turn = True

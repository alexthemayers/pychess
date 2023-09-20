import uuid
from typing import Dict, List
from uuid import uuid4, UUID

import uvicorn
from fastapi import FastAPI, Header

from chess.lib.active_game import ActiveInstance
from chess.lib.board import Board
from chess.lib.game import Game
from chess.lib.player import Player
from chess.lib.team import TeamEnum

gamesList = Dict[str, ActiveInstance]


def run(host: str, port: int):
    app = FastAPI()
    # Store chess games and their respective boards in memory (a simple dictionary)
    games: gamesList = {}
    register_routes(app, games)
    uvicorn.run(app, host=host, port=port)


def register_routes(app: FastAPI, games: gamesList):
    @app.post("/new_game")
    def new_game_handler(name: str, team: str):
        """
        TODO should take player teams, names, tokens. Create player objects, create Game(player1=player1, player2=None)
        TODO should return a basic game id for others to use for connection
        :param name:
        :param team:
        :return:
        """
        # input validation
        if len(team) != 5 or team.upper() not in TeamEnum.__members__:
            return {"error": f"{team} is not a valid team. choose either 'black' or 'white'"}, 400
        if len(name) > 64:
            return {"error": f"name is too long. names must be 64 characters or less"}, 400

        # setup values needed for identification
        game_id: UUID = uuid4()
        token: UUID = uuid4()
        if game_id in games:
            return {"message": "Game already exists"}

        # create game in memory with player and new board
        games[str(game_id)] = ActiveInstance(Game(Player(name, team)), Board(), token)
        header = {"token": f"Bearer {str(token)}"}
        return {}, 204, header

    @app.get("/games")
    def list_games_handler():
        """
        returns the ids of games that are waiting to be joined
        :return:
        """
        return {[game_id for game_id in games.keys() if games.get(game_id).is_waiting()]}, 200

    # result = [element for triple in data for sub_tuple in triple for element in sub_tuple]

    @app.post("/make_move/{game_id}")
    def make_move(game_id: str, move: List[str], token=Header(None)):
        if game_id not in games:
            return {"message": "Game not found"}, 404
        game = games.get(game_id)
        if game.token() != uuid.UUID(token):
            return {"error", "not authorised to enter this game"}, 401

        # Check if the game is over
        if game.winner() is not None:
            return {"message": "Game over", "winner": game.winner()}, 420

        return {"message": "Move accepted", "state": game.state()}, 200

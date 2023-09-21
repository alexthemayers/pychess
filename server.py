from typing import Dict, Tuple
from uuid import uuid4, UUID

import uvicorn
from fastapi import FastAPI, Header

from chess import (
    ActiveInstance,
    Board,
    move_is_possible,
    populate_board,
    is_move_primitive,
    Player,
    TeamEnum
)

gamesList = Dict[str, ActiveInstance]


def run(host: str, port: int):
    app = FastAPI()
    # Store chess games and their respective boards in memory (a simple dictionary)
    games: gamesList = {}
    register_routes(app, games)
    uvicorn.run(app, host=host, port=port)


def register_routes(app: FastAPI, active_game_instances: gamesList):
    @app.post("/new_game")
    def new_game_handler(name: str, team: str):
        """
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
        if game_id in active_game_instances:
            return {"message": "game already exists"}, 409

        # create game in memory with player and new board
        new_game_instance = ActiveInstance(Board(), token)
        new_game_instance.add_player(Player(name, team))
        active_game_instances[str(game_id)] = new_game_instance
        header = {"token": f"Bearer {str(token)}"}
        return {"game_id": game_id}, 204, header

    @app.post("/join_game/{game_id}")
    def join_game_handler(game_id: str, name: str, team: str):
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
        token: UUID = uuid4()

        # create game in memory with player and new board
        if not str(game_id) in active_game_instances.keys():
            return {"error": f"cannot find game with id {game_id}"}, 404
        game = active_game_instances[str(game_id)]
        game.add_player(Player(name, team))
        header: Dict[str, str] = {"token": f"Bearer {str(token)}"}
        if not game.is_waiting_for_players():
            populate_board(game.board(), game.players())
            return {"message": "game started", "new_game_state": game.json_state()}, 204, header
        return {}, 500

    @app.get("/games")
    def list_games_handler():
        """
        returns the ids of games that are waiting to be joined
        :return:
        """
        return {"waiting_games": {game_id for game_id in active_game_instances.keys() if
                                  active_game_instances.get(game_id).is_waiting_for_players()}}, 200

    @app.post("/make_move/{game_id}")
    def make_move(game_id: str, move: Tuple[str, str], token=Header()):

        # validation
        if len(move) != 2 or not is_move_primitive(move):
            return {"error": "move not properly formatted"}, 400

        # find game
        if game_id not in active_game_instances:
            return {"message": "game not found"}, 404
        game_instance = active_game_instances.get(game_id)

        # authorization
        wanted_token = str(game_instance.token())
        actual_token = token.removeprefix("Bearer ")
        if wanted_token != actual_token:
            return {"error", "not authorised to enter this game"}, 401

        # move validation
        current_player = game_instance.current_player()
        board = game_instance.board()
        piece_to_move = board.get_piece(move[0])
        current_player_owns_piece = piece_to_move.get_team() == current_player.team
        if not current_player_owns_piece:
            return {"error", "this piece is not owned by you"}, 400
        if not move_is_possible(piece_to_move, board, move):
            return {"error", "that move is not possible"}, 400
        # if causes_check():
        #     return {"error", "that move puts you in check"}, 400

        # move
        board.move(move)
        # Check if the game is over
        if game_instance.winner() is not None:
            return {"message": "game over", "winner": game_instance.winner()}, 420
        game_instance.rotate_players()
        return {"message": "move accepted", "new_game_state": game_instance.json_state()}, 200

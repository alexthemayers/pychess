import uvicorn
from fastapi import FastAPI
from typing import Tuple

from chess.board import Board

app = FastAPI()

# Store chess games in memory (a simple dictionary)
games = {}


@app.post("/new_game")
def new_game(game_id: str):
    if game_id in games:
        return {"message": "Game already exists"}

    games[game_id] = Board()
    return {"message": f"New game created.", "id": game_id}


@app.post("/make_move/{game_id}")
def make_move(game_id: str, move: Tuple[str, str]):
    if game_id not in games:
        return {"message": "Game not found"}

    # Get the game board
    board = games[game_id]

    # Check if the game is over
    if board.is_game_over():
        return {"message": "Game over", "result": board.result()}

    return {"message": "Move accepted"}


def run(host: str, port: int):
    uvicorn.run(app, host=host, port=port)

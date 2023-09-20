import uuid
from typing import Tuple

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from server import register_routes

app = FastAPI()
games = {}
register_routes(app, games)
client = TestClient(app)


@pytest.fixture
def mock_active_game_instances():
    # Implement a fixture to mock the 'active_game_instances' dictionary.
    # You can use this to control the state of your games for testing.
    pass


def test_new_game_endpoint():
    # Test the /new_game endpoint.
    # TODO we wanted these to be in the body
    # successful creations
    response = client.post("/new_game?name=Player1&team=white")
    assert response.status_code == 200
    assert response.json()[2].get("token") != ""

    response = client.post("/new_game?name=Player1&team=black")
    assert response.status_code == 200
    assert response.json()[2].get("token") != ""

    # no player
    response = client.post("/new_game?team=white")
    assert response.status_code == 422
    assert response.json().get("detail")[0].get("loc") == ['query', 'name']

    # no team
    response = client.post("/new_game?name=Player1")
    assert response.status_code == 422
    assert response.json().get("detail")[0].get("loc") == ['query', 'team']

    # check that team validation works correctly
    # TODO fix this
    # response = client.post("/new_game?name=Player1&team=blue")
    # assert response.json().get("detail")[0].get("loc") == ['query', 'team']
    # assert response.status_code == 400
    # Add assertions to check the response content or headers as needed.


def test_join_game_endpoint():
    # Test the /join_game/{game_id} endpoint.
    # try to join a game that does not exist
    want_game_id = uuid.uuid4()
    response = client.post(f"/join_game/{want_game_id}?name=Player2&team=black")
    assert response.json() == [{"error": f"cannot find game with id {want_game_id}"}, 404]

    # create a game to join
    response = client.post("/new_game?name=Player1&team=white")
    body, status, headers = response.json()
    assert body.get("game_id") != ""
    assert status == 204
    assert headers.get('token') != ""
    game_id: str = body.get("game_id")

    # attempt to join that game
    response = client.post(f"/join_game/{game_id}?name=Player2&team=black")
    body, status, headers = response.json()
    assert status == 204
    assert headers.get("token") != ""
    assert body.get("message") == "game started"
    assert type(body.get("new_game_state")) == dict
    assert response.status_code == 200
    # Add assertions to check the response content or headers as needed.


def test_list_games_endpoint():
    # Test the /games endpoint.
    response = client.post("/new_game?name=Player1&team=white")
    body, status, headers = response.json()
    game_id_1 = body.get("game_id")
    response = client.post("/new_game?name=Player2&team=black")
    body, status, headers = response.json()
    game_id_2 = body.get("game_id")
    response = client.post("/new_game?name=Player1&team=black")
    body, status, headers = response.json()
    game_id_3 = body.get("game_id")

    response = client.get("/games")
    body, status = response.json()
    assert status == 200
    assert game_id_1 in body.get("waiting_games")
    assert game_id_2 in body.get("waiting_games")
    assert game_id_3 in body.get("waiting_games")
    # Add assertions to check the response content.


def test_make_move_endpoint():
    # Test the /make_move/{game_id} endpoint.
    # create a game to join
    response = client.post("/new_game?name=Player1&team=white")
    body, status, headers = response.json()
    assert status == 204
    game_id = body.get("game_id")
    token = headers.get('token')
    # attempt to join that game
    response = client.post(f"/join_game/{game_id}?name=Player2&team=black")
    body, status, headers = response.json()
    assert status == 204
    move: Tuple[str, str] = ("b2", "b4")
    response = client.post(f"/make_move/{game_id}", json=move, headers={"token": f"{token}"})
    body, status = response.json()
    assert status == 200
    assert body.get("message") == "move accepted"
    assert body.get("new_game_state").get("board").get("b4") == {"type": "Pawn", "team": "white", "has_moved": False}

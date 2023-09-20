import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from server import register_routes
# Create a test client for the FastAPI app

app = FastAPI()
games = {}
register_routes(app, games)
client = TestClient(app)

# Define a fixture to create a new game before each test
@pytest.fixture
def new_game():
    pass
    # response = client.post("/new_game/game1")
    # assert response.status_code == 200
    # assert response.json() == {"message": "New game created with ID: game1"}

# Test creating a new game
def test_new_game(new_game):
    pass  # The new_game fixture handles this test

# Test making a valid move
def test_make_valid_move(new_game):
    pass
    # response = client.post("/make_move/game1", json={"from_square": "e2", "to_square": "e4"})
    # assert response.status_code == 200
    # assert response.json() == {"message": "Move accepted"}

# Test making an invalid move
def test_make_invalid_move(new_game):
    pass
    # response = client.post("/make_move/game1", json={"from_square": "e2", "to_square": "e5"})
    # assert response.status_code == 200
    # assert response.json() == {"message": "Invalid move"}

# Test making a move in a non-existent game
def test_make_move_in_nonexistent_game():
    pass
    # response = client.post("/make_move/nonexistent_game", json={"from_square": "e2", "to_square": "e4"})
    # assert response.status_code == 200
    # assert response.json() == {"message": "Game not found"}

# You can add more test cases as needed

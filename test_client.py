from unittest.mock import AsyncMock, Mock

import pytest
from loguru import logger

from client import (
    Client,
    new_game,
    join_game,
    move,
    list_waiting_games,
    game_is_waiting,
)


@pytest.fixture
def mock_client():
    return Client("http://mocked-host")


@pytest.mark.asyncio
async def test_new_game(mock_client):
    pytest.skip("fixme")
    expected_response = {
        "game_id": "12345",
    }
    mock_client.post = AsyncMock(return_value=Mock(json=AsyncMock(return_value=expected_response)))

    game_id, token = await new_game(mock_client, logger, "John", "TeamA")

    assert game_id is "12345"
    assert token is not None


@pytest.mark.asyncio
async def test_join_game(mock_client):
    pytest.skip("fixme")
    expected_response = {
        "new_game_state": {
            "board": [["X", "O", "X"], ["O", "", ""], ["", "", "X"]]
        }
    }
    mock_client.post = AsyncMock(
        return_value=Mock(headers={"token": "Bearer ABC123"}, json=AsyncMock(return_value=expected_response)))

    token, board = await join_game(mock_client, logger, "game123", "Alice", "TeamB")

    assert token == "ABC123"
    assert board == [["X", "O", "X"], ["O", "", ""], ["", "", "X"]]


@pytest.mark.asyncio
async def test_move(mock_client):
    pytest.skip("fixme")
    expected_response = {
        "new_game_state": {
            "board": [["X", "O", "X"], ["O", "X", ""], ["", "", "X"]]
        }
    }
    mock_client.post = AsyncMock(return_value=Mock(json=AsyncMock(return_value=expected_response)))

    board = await move(mock_client, logger, "game123", ("1", "2"), "ABC123")

    assert board == [["X", "O", "X"], ["O", "X", ""], ["", "", "X"]]


@pytest.mark.asyncio
async def test_list_waiting_games(mock_client):
    pytest.skip("fixme")
    expected_response = ["game1", "game2", "game3"]
    mock_client.post = AsyncMock(return_value=Mock(json=AsyncMock(return_value=expected_response)))

    games = await list_waiting_games(mock_client, logger)

    assert games == expected_response


@pytest.mark.asyncio
async def test_game_is_waiting(mock_client):
    pytest.skip("fixme")
    expected_response = ["game1", "game2", "game3"]
    mock_client.post = AsyncMock(return_value=Mock(json=AsyncMock(return_value=expected_response)))

    game_id = "game2"
    result = await game_is_waiting(mock_client, logger, game_id)

    assert result is True

    game_id = "nonexistent_game"
    result = await game_is_waiting(mock_client, logger, game_id)

    assert result is False

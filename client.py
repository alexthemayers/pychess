import httpx
from loguru import logger
import time


class Client(httpx.AsyncClient):
    _host: str

    def __init__(self, host):
        super().__init__()
        self._host = host

    async def new_game(self, name: str, team: str) -> (dict, int, dict):
        response = await self.post(
            f"{self._host}/new_game?name={name}&team={team}"
        )
        response.raise_for_status()
        return response.json()

    async def join_game(self, game_id: str, name: str, team: str) -> (dict, int, dict):
        response = await self.post(
            f"{self._host}/join_game/{game_id}?name={name}&team={team}",
        )
        response.raise_for_status()
        return response.json()

    async def move(self, game_id: str, move_pair: tuple[str, str], token: str) -> (dict, int, dict):
        response = await self.post(
            f"{self._host}/make_move/{game_id}",
            json=move_pair,
            headers={"token": f"Bearer {token}"}
        )
        response.raise_for_status()
        return response.json()

    async def list_games(self) -> (dict, int, dict):
        response = await self.post(
            f"{self._host}/games",
        )
        response.raise_for_status()
        return response.json()


async def new_game(client: Client, log, name: str, team: str) -> (str, str):
    try:
        body, status, headers = await client.new_game(name, team)
        game_id = body.get("game_id")
        token = headers.get("token").removeprefix("Bearer ")
        return game_id, token
    except httpx.RequestError as e:
        log.error(f"Request error occurred: {e}")
    except httpx.HTTPStatusError as e:
        log.error(f"HTTP error occurred: {e}")
    except Exception as e:
        log.error(f"An error occurred: {e}")


async def join_game(client: Client, log, game_id: str, name: str, team: str) -> (str, dict):
    try:
        body, status, headers = await client.join_game(game_id, name, team)
        token = headers.get("token").removeprefix("Bearer ")
        board = body.get("new_game_state").get("board")
        # todo return board state
        return token, board
    except httpx.RequestError as e:
        log.error(f"Request error occurred: {e}")
    except httpx.HTTPStatusError as e:
        log.error(f"HTTP error occurred: {e}")
    except Exception as e:
        log.error(f"An error occurred: {e}")


async def move(client: Client, log, game_id: str, move_pair: tuple[str, str], token: str) -> dict:
    try:
        body, status, headers = await client.move(game_id, move_pair, token)
        board = body.get("new_game_state").get("board")
        return board
    except httpx.RequestError as e:
        log.error(f"Request error occurred: {e}")
    except httpx.HTTPStatusError as e:
        log.error(f"HTTP error occurred: {e}")
    except Exception as e:
        log.error(f"An error occurred: {e}")


async def list_waiting_games(client: Client, log) -> list[str]:
    try:
        body, status, headers = await client.list_games()
        return body
    except httpx.RequestError as e:
        log.error(f"Request error occurred: {e}")
    except httpx.HTTPStatusError as e:
        log.error(f"HTTP error occurred: {e}")
    except Exception as e:
        log.error(f"An error occurred: {e}")


async def game_is_waiting(client: Client, log, game_id: str) -> bool:
    games = await list_waiting_games(client, log)
    return game_id in games


async def run(host: str, port: str | None):
    if port is not None:
        host = f"{host}:{str(port)}"
    async with Client(host) as client:
        name_player1 = "player1"
        name_player2 = "player2"
        team_white = "white"
        team_black = "black"

        # create a game
        # TODO implement token identity
        game_id, token = await new_game(client, logger, name_player1, team_white)
        # join game
        await join_game(client, logger, game_id, name_player2, team_black)
        while True:
            if not game_is_waiting(client, logger, game_id):
                break
            time.sleep(2)

        # move

        board = await move(client, logger, game_id, ("b2", "b4"), token)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run("http://localhost", 8000))

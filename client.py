import httpx


async def run(host: str):
    async with httpx.AsyncClient() as client:
        name_player1 = "player1"
        name_player2 = "player2"
        team_white = "white"
        team_black = "black"
        # create a game
        response = await client.post(
            f"{host}/new_game?name={name_player1}&team={team_white}"
        )
        body, status, headers = response.json()
        game_id = body.get("game_id")
        token = headers.get("token").removeprefix("Bearer ")
        print(response.text)
        response = await client.post(
            f"{host}/join_game/{game_id}?name={name_player2}&team={team_black}",
        )
        print(response.text)
        move: tuple[str, str] = ("b2", "b4")
        response = await client.post(f"{host}/make_move/{game_id}", json=move, headers={"token": f"{token}"})
        body, status = response.json()
        assert status == 200


if __name__ == "__main__":
    import asyncio

    asyncio.run(run("http://localhost"))

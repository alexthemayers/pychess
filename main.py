import argparse

from client import run as client_run
from server import run as server_run
from standalone import run as standalone_run

SERVER_ARG = "server"
CLIENT_ARG = "client"

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Main file for chess server or client")
    parser.add_argument("arg1", type=str, default=None,
                        help="can be set to client or server to initialise that functionality")
    parser.add_argument("--host", type=str, default="0.0.0.0",
                        help="the host ip that the server will run on")
    parser.add_argument("--port", type=int, default=8000,
                        help="the port that the server will run on")
    args = parser.parse_args()
    if args.arg1 is None:
        standalone_run()
    client_or_server: str = args.arg1
    if client_or_server == CLIENT_ARG:
        if args.host is not None:
            host: str = args.host
            import asyncio

            asyncio.run(client_run("http://localhost:8000"))
    if client_or_server == SERVER_ARG:
        if args.host and args.port is not None:
            host: str = args.host
            port: int = args.port
            server_run(host, port)

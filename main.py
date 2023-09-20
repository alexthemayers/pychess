import argparse

from client import run as client_run
from server import run as server_run
from standalone import run as standalone_run

SERVER_ARG = "server"
CLIENT_ARG = "client"

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Main file for chess server or client")
    parser.add_argument("arg1", type=str, default=None, help="if set, client will run")
    parser.add_argument("--client", type=bool, default=False, help="if set, client will run")
    parser.add_argument("--server", type=bool, default=False, help="if set, server will run")
    args = parser.parse_args()
    if args.arg1 is None:
        standalone_run()
    client_or_server: str = args.arg1
    if client_or_server == CLIENT_ARG:
        if args.host is not None:
            host: str = args.host
            client_run(host)
    if client_or_server == SERVER_ARG:
        if args.host and args.port is not None:
            host: str = args.host
            port: int = args.port
            server_run(host, port)

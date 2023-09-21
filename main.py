import argparse
import sys
from loguru import logger

from client import run as client_run
from server import run as server_run
from standalone import run as standalone_run


def check_host_port(arg_parser: argparse.ArgumentParser, host: str, port: int):
    if port is None:
        arg_parser.print_help()
        sys.exit(2)
    if host is None:
        arg_parser.print_help()
        sys.exit(2)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Main file for chess server or client")
    parser.add_argument("mode", type=str, default=None,
                        help="can be set to client, server or standalone-gui.")
    parser.add_argument("--host", type=str, default=None,
                        help="the host ip that the server will run on or client will connect to. "
                             "required if server or client mode is set")
    parser.add_argument("--port", type=int, default=None,
                        help="the port that the server will run on or client will listen on"
                             "required if server or client mode is set")
    args = parser.parse_args()
    mode: str = args.mode
    match mode:
        case "client":
            check_host_port(parser, args.host, args.port)
            import asyncio

            logger.info(f"starting client for {args.host}:{str(args.port)}")
            asyncio.run(client_run(args.host, args.port))
            logger.info("successfully exited")
            sys.exit(0)
        case "server":
            check_host_port(parser, args.host, args.port)
            logger.info(f"starting server on {args.host}:{str(args.port)}")
            server_run(args.host, args.port)
            logger.info("successfully exited")
            sys.exit(0)
        case "standalone_gui":
            logger.info("starting standalone client")
            standalone_run()
            logger.info("successfully exited")
            sys.exit(0)
    parser.print_help()
    sys.exit(2)

from Player import *
from Constants import *
from typing import Dict, Tuple
from Board import *


class Piece():  # base class for all pieces

    def __init__(self, piece_type: str, player: Player):
        self.type = piece_type.lower()
        self.player = player
        self.team = self.player.team

    def __repr__(self) -> str:
        return f"{str(self.type)}"


class PieceHelper:
    board_generated: bool = False

    @classmethod
    def generate_pieces(cls, board: Board) -> Optional[Board]:
        if not cls.board_generated:  # check to see if previously run and short circuit if true
            assert len(PlayerHelper.players) == 2, "two players must have been created for a board to be generated"

        def __place_pawn_piece(p: Board.BoardPoint, team: Team) -> None:
            players: Dict[Team, Player] = {p.team: p for p in PlayerHelper.players}
            assert str(p).endswith("7") or str(p).endswith(
                "2"), "Pawn pieces should not be placed on rows other than 7 or 2"
            p.set_piece(Rook(players[team]))

        def __place_non_pawn_piece(p: Board.BoardPoint, team: Team) -> None:
            players: Dict[Team, Player] = {p.team: p for p in PlayerHelper.players}
            assert str(p).endswith("8") or str(p).endswith(
                "1"), "Non-pawn pieces should not be placed on rows other than 8 or 1"
            if str(p).startswith(("a", "h")):  # R
                p.set_piece(Rook(players[team]))
            elif str(p).startswith(("b", "g")):  # N
                p.set_piece(Knight(players[team]))
            elif str(p).startswith(("c", "f")):  # B
                p.set_piece(Bishop(players[team]))
            elif str(p).startswith("d"):  # Q
                p.set_piece(Queen(players[team]))
            elif str(p).startswith("e"):  # K
                p.set_piece(King(players[team]))
            else:
                print(f"point {str(p)} should not be present on board")

        for point in board.points:
            if str(point).endswith("8"):  # black pieces
                __place_non_pawn_piece(point, Team.TEAM_BLACK)
            elif str(point).endswith("7"):  # black pawns
                __place_pawn_piece(point, Team.TEAM_BLACK)
            elif str(point).endswith("2"):  # white pawns
                __place_pawn_piece(point, Team.TEAM_WHITE)
            elif str(point).endswith("1"):  # white pieces
                __place_non_pawn_piece(point, Team.TEAM_WHITE)
            else:
                print(f"invalid point {point.name} present in board")
                exit(1)
            return board
        else:
            pass


class Rook(Piece):

    def __init__(self, player):
        super().__init__(self.__name__, player)

    def __repr__(self) -> str:
        return super.__repr__(self)


class Bishop(Piece):

    def __init__(self, player):
        super().__init__(self.__name__, player)

    def __repr__(self) -> str:
        return super.__repr__(self)


class Knight(Piece):

    def __init__(self, player):
        super().__init__(self.__name__, player)

    def __repr__(self) -> str:
        return super.__repr__(self)


class King(Piece):

    def __init__(self, player):
        super().__init__(self.__name__, player)

    def __repr__(self) -> str:
        return super.__repr__(self)


class Queen(Piece):

    def __init__(self, player):
        super().__init__(self.__name__, player)

    def __repr__(self) -> str:
        return super.__repr__(self)


class Pawn(Piece):

    def __init__(self, player):
        super().__init__(self.__name__, player)

    def __repr__(self) -> str:
        return super.__repr__(self)


if __name__ == "__main__":
    print("run main.py")
    exit(1)

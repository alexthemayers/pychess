from enum import Enum
from typing import Tuple

from player import Player


class PieceType(Enum):
    KING = 1
    QUEEN = 2
    BISHOP = 3
    KNIGHT = 4
    ROOK = 5
    PAWN = 6

    def __repr__(self) -> str:
        return self.name.title()


class PieceColour(Enum):
    BLACK = 1
    WHITE = 2

    def __repr__(self) -> str:
        return self.name.title()


class Piece:  # base class for all pieces
    type: PieceType
    colour: PieceColour
    player: Player

    def __init__(self, player: Player):
        self.player = player

    def __repr__(self):
        return f"{self.type}"

    def has_moved(self) -> bool:
        pass

    def get_team(self) -> str:
        return self.player.team.lower()

    def can_move(self, move: Tuple[str, str]) -> bool:
        pass


class Rook(Piece):
    castled: bool = False

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.ROOK

    def __repr__(self) -> str:
        return str(self.type)


class Bishop(Piece):
    # TODO handle blocking pieces on board
    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.BISHOP

    def __repr__(self) -> str:
        return str(self.type)


class Knight(Piece):

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.KNIGHT

    def __repr__(self) -> str:
        return str(self.type)


class King(Piece):
    castled: bool = False

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.KING

    def __repr__(self) -> str:
        return str(self.type)


class Queen(Piece):
    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.QUEEN

    def __repr__(self) -> str:
        return str(self.type)


class Pawn(Piece):
    _has_moved: bool = False

    def has_moved(self) -> bool:
        return self._has_moved

    def set_has_moved(self) -> None:
        if self._has_moved is not False:
            raise RuntimeError()
        self._has_moved = True

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.PAWN

    def __repr__(self) -> str:
        return str(self.type)

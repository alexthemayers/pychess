from enum import Enum
from typing import Dict

from chess.player import Player


class PieceType(Enum):
    KING = "King"
    QUEEN = "Queen"
    BISHOP = "Bishop"
    KNIGHT = "Knight"
    ROOK = "Rook"
    PAWN = "Pawn"

    def __repr__(self) -> str:
        return self.name.title()


class Piece:  # base class for all pieces
    type: PieceType
    player: Player

    def __init__(self, player: Player):
        self.player = player

    def get_team(self) -> str:
        return self.player.team.lower()

    def to_obj(self) -> Dict[str, str | bool]:
        return {"type": self.type.value,
                "team": self.get_team()}


class Rook(Piece):
    castled: bool = False

    def to_obj(self) -> dict[str, str | bool]:
        return {"type": self.type.value,
                "team": self.get_team(),
                "castled": self.castled}

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.ROOK

    def __repr__(self):
        return f"{self.type.value}"


class Bishop(Piece):

    # TODO handle blocking pieces on board
    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.BISHOP

    def __repr__(self):
        return f"{self.type.value}"


class Knight(Piece):

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.KNIGHT

    def __repr__(self):
        return f"{self.type.value}"


class King(Piece):
    castled: bool = False

    def to_obj(self) -> dict[str, str | bool]:
        return {"type": self.type.value,
                "team": self.get_team(),
                "castled": self.castled}

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.KING

    def __repr__(self):
        return f"{self.type.value}"


class Queen(Piece):

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.QUEEN

    def __repr__(self):
        return f"{self.type.value}"


class Pawn(Piece):
    _has_moved: bool = False

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.PAWN

    def __repr__(self):
        return f"{self.type.value}"

    def has_moved(self) -> bool:
        """
        returns the has_moved boolean from a pawn instance
        :return:
        """
        return self._has_moved

    def set_has_moved(self) -> None:
        """
        sets the has_moved boolean on a pawn. This will result in a Runtime Exception if called more than once on the
        same pawn.
        :return:
        """
        if self._has_moved is not False:
            raise RuntimeError()
        self._has_moved = True

    def to_obj(self) -> dict[str, str | bool]:
        return {"type": self.type.value,
                "team": self.get_team(),
                "has_moved": self.has_moved()}

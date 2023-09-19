from enum import Enum

from player import Player


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
    player: Player

    def __init__(self, player: Player):
        self.player = player

    def get_team(self) -> str:
        return self.player.team.lower()


class Rook(Piece):
    castled: bool = False
    type: PieceType

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.ROOK

    def __repr__(self):
        return f"{self.type.value}"


class Bishop(Piece):
    type: PieceType

    # TODO handle blocking pieces on board
    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.BISHOP

    def __repr__(self):
        return f"{self.type.value}"


class Knight(Piece):
    type: PieceType

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.KNIGHT

    def __repr__(self):
        return f"{self.type.value}"


class King(Piece):
    type: PieceType
    castled: bool = False

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.KING

    def __repr__(self):
        return f"{self.type.value}"


class Queen(Piece):
    type: PieceType

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.QUEEN

    def __repr__(self):
        return f"{self.type.value}"


class Pawn(Piece):
    type: PieceType
    _has_moved: bool = False

    def __init__(self, player):
        super().__init__(player)
        self.type = PieceType.PAWN

    def __repr__(self):
        return f"{self.type.value}"

    def has_moved(self) -> bool:
        return self._has_moved

    def set_has_moved(self) -> None:
        if self._has_moved is not False:
            raise RuntimeError()
        self._has_moved = True

from typing import Optional

from piece import Piece


class _Block:
    position: str
    _piece: Optional[Piece]

    def __init__(self, position: str):
        self.position = position
        self._piece = None

    def get_piece(self) -> Optional[Piece]:
        return self._piece

    def set_piece(self, piece: Piece):
        self._piece = piece

    def clear_piece(self):
        self._piece = None

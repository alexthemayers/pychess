from chess.block import _Block
from chess.piece import Piece
from chess.player import Player


def test_block():
    position = "a1"
    block = _Block(position)
    assert block.get_piece() is None
    piece = Piece(Player("player name", "white"))
    block.set_piece(piece)
    assert block.get_piece() is not None
    assert block.get_piece() is piece
    block.clear_piece()
    assert block.get_piece() is None

from pytest import raises

from piece import (
    Piece,
    Pawn,
    King,
    Queen,
    Rook,
    Knight,
    Bishop
)
from player import Player


def test_peice_init():
    player1 = Player("test player", "white")
    piece1 = Piece(player1)
    player2 = Player("test player", "black")
    piece2 = Piece(player2)
    assert piece1.player is player1
    assert piece2.player is player2
    assert piece1.get_team() == "white"
    assert piece2.get_team() == "black"


def test_pawn_init():
    player = Player("test player", "white")
    pawn = Pawn(player)
    assert pawn.player is player
    assert not pawn.has_moved()
    assert pawn.get_team() == "white"
    assert str(pawn) == "Pawn"


def test_pawn_set_has_moved():
    player = Player("test player", "white")
    pawn = Pawn(player)
    assert not pawn.has_moved()
    pawn.set_has_moved()
    assert pawn.has_moved()
    with raises(RuntimeError):
        pawn.set_has_moved()
    assert pawn.has_moved()


def test_queen_init():
    player = Player("test player", "black")
    queen = Queen(player)
    assert queen.player is player
    assert queen.get_team() == "black"
    assert str(queen) == "Queen"


def test_king_init():
    player = Player("test player", "white")
    king = King(player)
    assert king.player is player
    assert king.get_team() == "white"
    assert str(king) == "King"


def test_rook_init():
    player = Player("test player", "black")
    rook = Rook(player)
    assert rook.player is player
    assert rook.get_team() == "black"
    assert str(rook) == "Rook"


def test_bishop_init():
    player = Player("test player", "white")
    bishop = Bishop(player)
    assert bishop.player is player
    assert bishop.get_team() == "white"
    assert str(bishop) == "Bishop"


def test_knight_init():
    player = Player("test player", "black")
    knight = Knight(player)
    assert knight.player is player
    assert knight.get_team() == "black"
    assert str(knight) == "Knight"

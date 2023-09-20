from movement import (
    bishop_can_make,
    king_can_make,
    knight_can_make,
    rook_can_make,
    queen_can_make,
    pawn_can_make,
    close_enough_for_king,
)


def test_bishop_can_make():
    # Test valid diagonal move without blocking pieces
    assert bishop_can_make(("a1", "c3"))

    assert bishop_can_make(("a1", "d4"))

    assert not bishop_can_make(("a1", "e4"))

    assert not bishop_can_make(("a1", "a1"))
    # Test invalid non-diagonal move
    assert bishop_can_make(("a1", "b2"))


def test_king_can_make():
    # Test valid vertical move within king's range
    assert king_can_make(("e1", "e2"))

    # Test valid horizontal move within king's range
    assert king_can_make(("e1", "f1"))

    # Test valid diagonal move within king's range
    assert king_can_make(("e1", "f2"))

    # Test invalid move outside of king's range
    assert not king_can_make(("e1", "e4"))

    assert not king_can_make(("a1", "a1"))


def test_pawn_can_make():
    assert not pawn_can_make(("a1", "a1"), False, "white")
    assert not pawn_can_make(("a1", "a1"), True, "black")

    # Test one move forward, white team, not moved
    assert pawn_can_make(("a2", "a3"), False, "white")

    # Test one move forward, black team, not moved
    assert pawn_can_make(("a7", "a6"), False, "black")

    # Test two moves forward, white team, not moved
    assert pawn_can_make(("a2", "a4"), False, "white")

    # Test two moves forward, black team, not moved
    assert pawn_can_make(("a7", "a5"), False, "black")

    # Test one move forward, white team, moved
    assert pawn_can_make(("a2", "a3"), True, "white")

    # Test one move forward, black team, moved
    assert pawn_can_make(("a7", "a6"), True, "black")

    # Test two moves forward, white team, moved
    assert not pawn_can_make(("a2", "a4"), True, "white")

    # Test two moves forward, black team, moved
    assert not pawn_can_make(("a7", "a5"), True, "black")

    # Test take diagonal left, white team, not moved
    assert pawn_can_make(("b2", "a3"), False, "white")

    # Test take diagonal left, black team, not moved
    assert pawn_can_make(("b7", "a6"), False, "black")

    # Test take diagonal right, white team, not moved
    assert pawn_can_make(("a2", "b3"), False, "white")

    # Test take diagonal right, black team, not moved
    assert pawn_can_make(("a7", "b6"), False, "black")

    # Test take diagonal left, white team, moved
    assert pawn_can_make(("b2", "a3"), True, "white")

    # Test take diagonal left, black team, moved
    assert pawn_can_make(("b7", "a6"), True, "black")

    # Test take diagonal right, white team, moved
    assert pawn_can_make(("a2", "b3"), True, "white")

    # Test take diagonal right, black team, moved
    assert pawn_can_make(("a7", "b6"), True, "black")


def test_rook_can_make():
    assert not rook_can_make(("a1", "a1"))
    # Test valid horizontal move
    assert rook_can_make(("a1", "h1"))

    # Test valid vertical move
    assert rook_can_make(("a1", "a8"))

    # Test invalid diagonal move
    assert not rook_can_make(("a1", "b2"))


def test_queen_can_make():
    assert not queen_can_make(("a1", "a1"))
    # Test valid horizontal move
    assert queen_can_make(("a1", "h1"))

    # Test valid vertical move
    assert queen_can_make(("a1", "a8"))

    # Test valid diagonal move
    assert queen_can_make(("a1", "h8"))

    # Test invalid non-linear move
    assert not queen_can_make(("a1", "b3"))

    # Test invalid out-of-range move
    # TODO implement this sort of validation elsewhere
    assert not queen_can_make(("a1", "a9"))


def test_knight_can_make():
    assert not knight_can_make(("a1", "a1"))
    # Test valid move
    assert knight_can_make(("a1", "c2"))

    assert knight_can_make(("b3", "c5"))

    assert knight_can_make(("f4", "h3"))
    # Test invalid non-linear move

    assert not knight_can_make(("d1", "e2"))

    # Test invalid out-of-range move
    # TODO implement this sort of validation elsewhere
    assert not queen_can_make(("a8", "c9"))


def test_close_enough_for_king():
    # Test valid close-enough move
    assert close_enough_for_king(("a1", "b2"))

    # Test invalid move with greater distance
    assert not close_enough_for_king(("a1", "c3"))

    # Test invalid move with diagonal distance
    assert not close_enough_for_king(("a1", "b3"))

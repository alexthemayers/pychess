from movement import (
    bishop_can_make,
    king_can_make,
    knight_can_make,
    rook_can_make,
    queen_can_make,
    close_enough_for_king,
)


def test_bishop_can_move():
    # Test valid diagonal move without blocking pieces
    assert bishop_can_make(("a1", "c3")) is True

    assert bishop_can_make(("a1", "d4")) is True

    assert bishop_can_make(("a1", "e4")) is False

    # Test invalid non-diagonal move
    assert bishop_can_make(("a1", "b2")) is True


def test_king_can_move():
    # Test valid vertical move within king's range
    assert king_can_make(("e1", "e2")) is True

    # Test valid horizontal move within king's range
    assert king_can_make(("e1", "f1")) is True

    # Test valid diagonal move within king's range
    assert king_can_make(("e1", "f2")) is True

    # Test invalid move outside of king's range
    assert king_can_make(("e1", "e4")) is False


def test_rook_can_move():
    # Test valid horizontal move
    assert rook_can_make(("a1", "h1")) is True

    # Test valid vertical move
    assert rook_can_make(("a1", "a8")) is True

    # Test invalid diagonal move
    assert rook_can_make(("a1", "b2")) is False


def test_queen_can_move():
    # Test valid horizontal move
    assert queen_can_make(("a1", "h1")) is True

    # Test valid vertical move
    assert queen_can_make(("a1", "a8")) is True

    # Test valid diagonal move
    assert queen_can_make(("a1", "h8")) is True

    # Test invalid non-linear move
    assert queen_can_make(("a1", "b3")) is False

    # Test invalid out-of-range move
    # TODO implement this sort of validation
    # assert queen_can_move(("a1", "a9")) is False


def test_knight_can_move():
    # Test valid move
    assert knight_can_make(("a1", "c2")) is True

    assert knight_can_make(("b3", "c5")) is True

    assert knight_can_make(("f4", "h3")) is True
    # Test invalid non-linear move

    assert knight_can_make(("d1", "e2")) is False

    # Test invalid out-of-range move
    # TODO implement this sort of validation
    # assert queen_can_move(("a8", "c9")) is False


def test_close_enough_for_king():
    # Test valid close-enough move
    assert close_enough_for_king(("a1", "b2")) is True

    # Test invalid move with greater distance
    assert close_enough_for_king(("a1", "c3")) is False

    # Test invalid move with diagonal distance
    assert close_enough_for_king(("a1", "b3")) is False

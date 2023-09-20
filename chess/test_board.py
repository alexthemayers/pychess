import json

from chess.board import Board, populate_board
from chess.piece import Piece
from chess.player import Player


def test_board_creation():
    # Test if a Board instance can be created
    board = Board()
    assert isinstance(board, Board)


def test_board_repr():
    # Test the __repr__ method to check if it returns a string representation of the board
    board = Board()
    expected_repr = (
        ' \tA\tB\tC\tD\tE\tF\tG\tH\n\n'
        '8\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
        '7\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
        '6\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
        '5\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
        '4\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
        '3\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
        '2\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
        '1\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
    )
    assert repr(board) == expected_repr


def test_board_repr_with_pieces():
    # Test the __repr__ method to check if it returns a string representation of the board
    player1 = Player("test name", "white")
    player2 = Player("test name", "black")
    board = Board()
    populate_board(board, [player1, player2])
    expected_repr = (' \tA\tB\tC\tD\tE\tF\tG\tH\n\n'
                     '8\tRO\tKN\tBI\tQU\tKI\tBI\tKN\tRO\n\n'
                     '7\tPA\tPA\tPA\tPA\tPA\tPA\tPA\tPA\n\n'
                     '6\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
                     '5\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
                     '4\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
                     '3\t__\t__\t__\t__\t__\t__\t__\t__\n\n'
                     '2\tPA\tPA\tPA\tPA\tPA\tPA\tPA\tPA\n\n'
                     '1\tRO\tKN\tBI\tQU\tKI\tBI\tKN\tRO\n\n')
    assert repr(board) == expected_repr


def test_position_to_index():
    # Test the _position_to_index method
    board = Board()
    assert board._position_to_index("a8") == 0
    assert board._position_to_index("h8") == 7
    assert board._position_to_index("a1") == 56
    assert board._position_to_index("h1") == 63


def test_index_to_position():
    board = Board()
    assert board._index_to_position(0) == "a8"
    assert board._index_to_position(7) == "h8"
    assert board._index_to_position(56) == "a1"
    assert board._index_to_position(63) == "h1"


def test_move_methods():
    # Test the move methods (e.g., north, south, east, west)
    board = Board()

    assert board.north("e4", 2) == "e6"
    assert board.north_east("e4", 2) == "g6"
    assert board.north_west("e4", 2) == "c6"
    assert board.south("e4", 3) == "e1"
    assert board.south_east("e4", 3) == "h1"
    assert board.south_west("e4", 3) == "b1"
    assert board.east("e4", 2) == "g4"
    assert board.west("e4", 1) == "d4"
    # Add more test cases for other move methods


def test_move():
    board = Board()
    player1 = Player("player1", "white")
    player2 = Player("player2", "black")
    populate_board(board, [player1, player2])
    before = "a2"
    after = "a4"
    piece = board.get_piece(before)
    board.move((before, after))
    assert board.get_piece(after) is piece
    assert board.get_piece(before) is None


def test_set_piece():
    # Test the set_piece method
    board = Board()
    player = Player("testname", "white")
    piece = Piece(player)  # Create a test piece

    # Set the piece at a specific position
    board.set_piece(piece, "e4")

    # Check if the piece is set correctly
    assert board.get_piece("e4") == piece


def test_is_blocked_diagonal():
    board = Board()
    player = Player("testname", "white")
    piece1 = Piece(player)  # Create a test piece
    piece2 = Piece(player)  # Create a test piece
    board.set_piece(piece1, "a1")
    board.set_piece(piece2, "c3")
    assert board.is_blocked_diagonal(("a1", "d4"))  # blocked by c3
    assert not board.is_blocked_diagonal(("a1", "b2"))  # starting point has piece
    assert not board.is_blocked_diagonal(("a1", "c3"))  # starting point and endpoint has piece
    assert not board.is_blocked_diagonal(("e1", "d2"))  # not blocked
    assert board.is_blocked_diagonal(("e1", "b4"))  # blocked by c3


def test_is_blocked_horizontal():
    board = Board()
    player = Player("testname", "white")
    piece1 = Piece(player)  # Create a test piece
    piece2 = Piece(player)  # Create a test piece
    board.set_piece(piece1, "a1")
    board.set_piece(piece2, "f1")
    assert board.is_blocked_horizontal(("a1", "g1"))  # blocked by f1
    assert not board.is_blocked_horizontal(("a1", "b1"))  # starting point has piece
    assert not board.is_blocked_horizontal(("a1", "f1"))  # starting point and endpoint has piece
    assert not board.is_blocked_horizontal(("b1", "e1"))  # not blocked
    assert board.is_blocked_horizontal(("d1", "g1"))  # blocked by f1


def test_is_blocked_vertical():
    board = Board()
    player = Player("testname", "white")
    piece1 = Piece(player)  # Create a test piece
    piece2 = Piece(player)  # Create a test piece
    board.set_piece(piece1, "a1")
    board.set_piece(piece2, "a7")
    assert board.is_blocked_vertical(("a1", "a8"))  # blocked by a7
    assert not board.is_blocked_vertical(("a1", "a2"))  # starting point has piece
    assert not board.is_blocked_vertical(("a1", "a7"))  # starting point and endpoint has piece
    assert not board.is_blocked_vertical(("b1", "b7"))  # not blocked
    assert board.is_blocked_vertical(("a5", "a8"))  # blocked by a7


def test_board_to_obj():
    board = Board()
    player1 = Player("testname", "white")
    player2 = Player("testname", "black")
    populate_board(board, [player1, player2])
    board_as_object = board.to_obj()
    assert board_as_object == {'a1': {'castled': False, 'team': 'white', 'type': 'Rook'},
                               'a2': {'has_moved': False, 'team': 'white', 'type': 'Pawn'},
                               'a3': {},
                               'a4': {},
                               'a5': {},
                               'a6': {},
                               'a7': {'has_moved': False, 'team': 'black', 'type': 'Pawn'},
                               'a8': {'castled': False, 'team': 'black', 'type': 'Rook'},
                               'b1': {'team': 'white', 'type': 'Knight'},
                               'b2': {'has_moved': False, 'team': 'white', 'type': 'Pawn'},
                               'b3': {},
                               'b4': {},
                               'b5': {},
                               'b6': {},
                               'b7': {'has_moved': False, 'team': 'black', 'type': 'Pawn'},
                               'b8': {'team': 'black', 'type': 'Knight'},
                               'c1': {'team': 'white', 'type': 'Bishop'},
                               'c2': {'has_moved': False, 'team': 'white', 'type': 'Pawn'},
                               'c3': {},
                               'c4': {},
                               'c5': {},
                               'c6': {},
                               'c7': {'has_moved': False, 'team': 'black', 'type': 'Pawn'},
                               'c8': {'team': 'black', 'type': 'Bishop'},
                               'd1': {'team': 'white', 'type': 'Queen'},
                               'd2': {'has_moved': False, 'team': 'white', 'type': 'Pawn'},
                               'd3': {},
                               'd4': {},
                               'd5': {},
                               'd6': {},
                               'd7': {'has_moved': False, 'team': 'black', 'type': 'Pawn'},
                               'd8': {'team': 'black', 'type': 'Queen'},
                               'e1': {'castled': False, 'team': 'white', 'type': 'King'},
                               'e2': {'has_moved': False, 'team': 'white', 'type': 'Pawn'},
                               'e3': {},
                               'e4': {},
                               'e5': {},
                               'e6': {},
                               'e7': {'has_moved': False, 'team': 'black', 'type': 'Pawn'},
                               'e8': {'castled': False, 'team': 'black', 'type': 'King'},
                               'f1': {'team': 'white', 'type': 'Bishop'},
                               'f2': {'has_moved': False, 'team': 'white', 'type': 'Pawn'},
                               'f3': {},
                               'f4': {},
                               'f5': {},
                               'f6': {},
                               'f7': {'has_moved': False, 'team': 'black', 'type': 'Pawn'},
                               'f8': {'team': 'black', 'type': 'Bishop'},
                               'g1': {'team': 'white', 'type': 'Knight'},
                               'g2': {'has_moved': False, 'team': 'white', 'type': 'Pawn'},
                               'g3': {},
                               'g4': {},
                               'g5': {},
                               'g6': {},
                               'g7': {'has_moved': False, 'team': 'black', 'type': 'Pawn'},
                               'g8': {'team': 'black', 'type': 'Knight'},
                               'h1': {'castled': False, 'team': 'white', 'type': 'Rook'},
                               'h2': {'has_moved': False, 'team': 'white', 'type': 'Pawn'},
                               'h3': {},
                               'h4': {},
                               'h5': {},
                               'h6': {},
                               'h7': {'has_moved': False, 'team': 'black', 'type': 'Pawn'},
                               'h8': {'castled': False, 'team': 'black', 'type': 'Rook'}}

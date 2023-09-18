from board import Board


# Replace 'your_module' with the actual name of the module where your Board class is defined

def test_board_creation():
    # Test if a Board instance can be created
    board = Board()
    assert isinstance(board, Board)


def test_board_repr():
    # Test the __repr__ method to check if it returns a string representation of the board
    board = Board()
    expected_repr = (
        "a8\tb8\tc8\td8\te8\tf8\tg8\th8\n"
        "a7\tb7\tc7\td7\te7\tf7\tg7\th7\n"
        "a6\tb6\tc6\td6\te6\tf6\tg6\th6\n"
        "a5\tb5\tc5\td5\te5\tf5\tg5\th5\n"
        "a4\tb4\tc4\td4\te4\tf4\tg4\th4\n"
        "a3\tb3\tc3\td3\te3\tf3\tg3\th3\n"
        "a2\tb2\tc2\td2\te2\tf2\tg2\th2\n"
        "a1\tb1\tc1\td1\te1\tf1\tg1\th1\n"
    )
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
    assert board.south("e4", 3) == "e1"
    assert board.east("e4", 2) == "g4"
    assert board.west("e4", 1) == "d4"
    # Add more test cases for other move methods


def test_set_piece():
    # Test the set_piece method
    from piece import Piece  # Import the Piece class if not already imported
    from player import Player
    board = Board()
    player = Player("testname", "white")
    piece = Piece(player)  # Create a test piece

    # Set the piece at a specific position
    board.set_piece(piece, "e4")

    # Check if the piece is set correctly
    assert board.get_piece("e4") == piece

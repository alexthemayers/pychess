from typing import List, Tuple, Optional, Dict

from chess.block import _Block
from chess.mapping import (
    calculate_horizontal_difference,
    calculate_vertical_difference, calculate_xy_difference
)
from chess.movement import (
    king_can_make,
    rook_can_make,
    queen_can_make,
    bishop_can_make,
    knight_can_make,
    pawn_can_make
)
from chess.piece import (
    Piece,
    Pawn,
    King,
    Queen,
    Rook,
    Bishop,
    Knight
)
from chess.player import Player

_BLOCK_NAMES: List[str] = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
                           "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                           "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
                           "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
                           "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
                           "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
                           "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                           "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]


class Board:
    _board: List[_Block]

    def get_board(self) -> List[_Block]:
        return self._board

    def __init__(self):
        self._board = [_Block(block) for block in _BLOCK_NAMES]

    def __repr__(self) -> str:
        ret: str = ' \tA\tB\tC\tD\tE\tF\tG\tH\n\n'
        idx = 9
        rows_left_to_print = 8
        # for name, block in self._board:
        for block in self._board:
            if idx % 8 == 1:
                ret += str(rows_left_to_print) + "\t"
                rows_left_to_print -= 1
            if block.get_piece() is None:
                ret += "__"
            else:
                ret += str(block.get_piece())[0:2].upper()
            if idx % 8 == 0 and idx > 15:
                ret += "\n\n"
            else:
                ret += "\t"
            idx += 1
        return ret

    def to_obj(self) -> Dict:
        return {b.position: b.get_piece().to_obj() if b.get_piece() is not None else {} for b in self.get_board()}

    def _position_to_index(self, position: str) -> int:
        """
        returns the index of the board list where the given position name can be found
        :param position:
        :return:
        """
        j: int = 0
        for block in self._board:
            if block.position == position:
                return j
            j += 1

    def _index_to_position(self, index: int) -> str:
        """
        returns the position name within the board list at the given index
        :param index:
        :return:
        """
        j: int = 0
        for block in self._board:
            if j == index:
                return block.position
            j += 1

    def north(self, current_position: str, y: int) -> str:
        """
        provides the position name at y steps north
        :param current_position:
        :param y:
        :return:
        """
        index: int = self._position_to_index(current_position)
        # TODO should not move off board
        index -= (8 * y)
        return self._index_to_position(index)

    def north_west(self, current_position: str, xy: int) -> str:
        """
        provides the position name at xy steps north west
        :param current_position:
        :param xy:
        :return:
        """
        index: int = self._position_to_index(current_position)
        # TODO should not move off board
        index -= (9 * xy)
        return self._index_to_position(index)

    def north_east(self, current_position: str, xy: int) -> str:
        """
        provides the position name at xy steps north east
        :param current_position:
        :param xy:
        :return:
        """
        index: int = self._position_to_index(current_position)
        # TODO should not move off board
        index -= (7 * xy)
        return self._index_to_position(index)

    def south(self, current_position: str, y: int) -> str:
        """
        provides the position name at y steps south
        :param current_position:
        :param y:
        :return:
        """
        index: int = self._position_to_index(current_position)
        # TODO should not move off board
        index += (8 * y)
        return self._index_to_position(index)

    def south_west(self, current_position: str, xy: int) -> str:
        """
        provides the position name at xy steps south west
        :param current_position:
        :param xy:
        :return:
        """
        index: int = self._position_to_index(current_position)
        # TODO should not move off board
        index += (7 * xy)
        return self._index_to_position(index)

    def south_east(self, current_position: str, xy: int) -> str:
        """
        provides the position name at xy steps south east
        :param current_position:
        :param xy:
        :return:
        """
        index: int = self._position_to_index(current_position)
        # TODO should not move off board
        index += (9 * xy)
        return self._index_to_position(index)

    def west(self, current_position: str, x: int) -> str:
        """
        provides the position name at x steps west
        :param current_position:
        :param x:
        :return:
        """
        index: int = self._position_to_index(current_position)
        # TODO should not wrap around
        index -= x
        return self._index_to_position(index)

    def east(self, current_position: str, x: int) -> str:
        """
        provides the position name at x steps east
        :param current_position:
        :param x:
        :return:
        """
        index: int = self._position_to_index(current_position)
        # TODO should not wrap around
        index += x
        return self._index_to_position(index)

    def set_piece(self, piece: Piece, position: str) -> None:
        """
        sets piece at given position on the board
        :param piece:
        :param position:
        :return:
        """
        for block in self._board:
            if block.position == position:
                block.set_piece(piece)

    def _is_clear_path(self, move: Tuple[str, str]) -> bool:
        # print("can move still needs to be implemented")
        pass

    def get_piece(self, position: str) -> Optional[Piece]:
        """
        get piece from given position on the board
        :param position:
        :return:
        """
        for block in self._board:
            if block.position == position:
                return block.get_piece()

    def move(self, move: Tuple[str, str]):
        """
        move assumes that all validation for a move has already been performed.
        It simply allows us to move the pieces required.
        :param move:
        :return:
        """
        before = move[0]
        after = move[1]
        piece = self.get_piece(before)
        self.set_piece(piece, after)
        self.clear_piece(before)
        pass

    def is_blocked_diagonal(self, move: Tuple[str, str]):
        current_loc = move[0]
        next_loc: Optional[str] = None
        last_loc = move[1]
        is_blocked: bool = False
        horizontal_difference, vertical_difference = calculate_xy_difference(move)
        if horizontal_difference == 0 or vertical_difference == 0:
            return False
        # we should not consider a piece at the end position to cause blocking, we take the piece in this case
        while True:
            if vertical_difference > 0 and horizontal_difference > 0:
                next_loc = self.north_east(current_loc, 1)
            if vertical_difference < 0 < horizontal_difference:
                next_loc = self.south_east(current_loc, 1)
            if vertical_difference > 0 > horizontal_difference:
                next_loc = self.north_west(current_loc, 1)
            if vertical_difference < 0 and horizontal_difference < 0:
                next_loc = self.south_west(current_loc, 1)
            # we don't check the last location as we may be taking a piece that resides there
            if next_loc != last_loc:
                if self.get_piece(next_loc) is not None:
                    is_blocked = True
            current_loc = next_loc
            if current_loc == last_loc or is_blocked:
                break
        return is_blocked

    def is_blocked_vertical(self, move: Tuple[str, str]):
        current_loc = move[0]
        last_loc = move[1]
        next_loc: Optional[str] = None
        is_blocked: bool = False
        vertical_difference = calculate_vertical_difference(current_loc, last_loc)
        if vertical_difference == 0:
            return False
        # we should not consider a piece at the end position to cause blocking, we take the piece in this case
        while True:
            if vertical_difference > 0:
                next_loc = self.north(current_loc, 1)
            if vertical_difference < 0:
                next_loc = self.south(current_loc, 1)
            # we don't check the last location as we may be taking a piece that resides there
            if next_loc != last_loc:
                if self.get_piece(next_loc) is not None:
                    is_blocked = True
            current_loc = next_loc
            if current_loc == last_loc or is_blocked:
                break
        return is_blocked

    def is_blocked_horizontal(self, move: Tuple[str, str]):
        current_loc = move[0]
        last_loc = move[1]
        next_loc: Optional[str] = None
        is_blocked: bool = False
        horizontal_difference = calculate_horizontal_difference(current_loc, last_loc)
        if horizontal_difference == 0:
            return False
        # we should not consider a piece at the end position to cause blocking, we take the piece in this case
        while True:
            if horizontal_difference > 0:
                next_loc = self.east(current_loc, 1)
            if horizontal_difference < 0:
                next_loc = self.west(current_loc, 1)
            # we don't check the last location as we may be taking a piece that resides there
            if next_loc != last_loc:
                if self.get_piece(next_loc) is not None:
                    is_blocked = True
            current_loc = next_loc
            if current_loc == last_loc or is_blocked:
                break
        return is_blocked

    def clear_piece(self, position: str):
        for block in self._board:
            if block.position == position:
                block.clear_piece()


def move_is_possible(piece: Piece, board: Board, move: Tuple[str, str]) -> bool:
    match piece:
        case Pawn() as pawn:
            return (pawn_can_make(move, pawn.has_moved(), pawn.get_team())
                    and not board.is_blocked_vertical(move)
                    and not board.is_blocked_horizontal(move)
                    and not board.is_blocked_diagonal(move))
        case King():
            return (king_can_make(move)
                    and not board.is_blocked_vertical(move)
                    and not board.is_blocked_horizontal(move)
                    and not board.is_blocked_diagonal(move))
        case Queen():
            return (queen_can_make(move)
                    and not board.is_blocked_vertical(move)
                    and not board.is_blocked_horizontal(move)
                    and not board.is_blocked_diagonal(move))
        case Rook():
            return (rook_can_make(move)
                    and not board.is_blocked_vertical(move)
                    and not board.is_blocked_horizontal(move))
        case Bishop():
            return (bishop_can_make(move)
                    and not board.is_blocked_diagonal(move))
        case Knight():
            # we don't need to check if the knight is blocked before moving
            return knight_can_make(move)


# TODO check out how this compromises the dependency heirarchy and find new home if necessary
def populate_board(board: Board, players: List[Player]) -> Board:
    players: Dict[str, Player] = {p.team: p for p in players}

    def __place_non_pawn_piece(b: _Block, team: str) -> None:
        if b.position.startswith(("a", "h")):  # R
            b.set_piece(Rook(players[team]))
        elif b.position.startswith(("b", "g")):  # N
            b.set_piece(Knight(players[team]))
        elif b.position.startswith(("c", "f")):  # B
            b.set_piece(Bishop(players[team]))
        elif b.position.startswith("d"):  # Q
            b.set_piece(Queen(players[team]))
        elif b.position.startswith("e"):  # K
            b.set_piece(King(players[team]))
        else:
            # TODO throw an error here
            print(f"point {b.position} should not be present on board")

    for b in board.get_board():
        if b.position.endswith("8"):
            __place_non_pawn_piece(b, "black")
        elif b.position.endswith("7"):
            b.set_piece(Pawn(players["black"]))
        elif b.position.endswith("2"):
            b.set_piece(Pawn(players["white"]))
        elif b.position.endswith("1"):
            __place_non_pawn_piece(b, "white")
    return board

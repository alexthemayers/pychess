from typing import List, Tuple, Optional

from block import _Block
from input import is_possible_vertical_move
from mapping import (
    calculate_horizontal_difference,
    calculate_vertical_difference, calculate_xy_difference
)
from movement import (
    king_can_make,
    rook_can_make,
    queen_can_make,
    bishop_can_make,
    knight_can_make
)
from piece import (
    Piece,
    Pawn,
    King,
    Queen,
    Rook,
    Bishop,
    Knight
)

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
        ret: str = ""
        idx = 1
        # for name, block in self._board:
        for block in self._board:
            if block.get_piece() is None:
                ret += block.position
            else:
                ret += str(block.get_piece())[0] + " "
            if idx % 8 == 0:
                ret += "\n"
            else:
                ret += "\t"
            idx += 1
        return ret

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
        current = move[0]
        end = move[1]
        is_blocked: bool = False
        vertical_difference = calculate_vertical_difference(current, end)
        horizontal_difference = calculate_horizontal_difference(current, end)
        # we should not consider a piece at the end position to cause blocking, we take the piece in this case
        while current != end or not is_blocked:
            if vertical_difference > 0 and horizontal_difference > 0:
                current = self.north_east(current, 1)
            if vertical_difference < 0 < horizontal_difference:
                current = self.south_east(current, 1)
            if vertical_difference > 0 > horizontal_difference:
                current = self.north_west(current, 1)
            if vertical_difference < 0 and horizontal_difference < 0:
                current = self.south_west(current, 1)
            if self.get_piece(current) is not None:
                is_blocked = True
        return is_blocked

    def is_blocked_vertical(self, move: Tuple[str, str]):
        current = move[0]
        end = move[1]
        is_blocked: bool = False
        vertical_difference = calculate_vertical_difference(current, end)
        # we should not consider a piece at the end position to cause blocking, we take the piece in this case
        while current != end or not is_blocked:
            if vertical_difference > 0:
                current = self.north(current, 1)
            if vertical_difference < 0:
                current = self.south(current, 1)
            if self.get_piece(current) is not None:
                is_blocked = True
        return is_blocked

    def is_blocked_horizontal(self, move: Tuple[str, str]):
        current = move[0]
        end = move[1]
        is_blocked: bool = False
        horizontal_difference = calculate_horizontal_difference(current, end)
        # we should not consider a piece at the end position to cause blocking, we take the piece in this case
        while current != end or not is_blocked:
            if horizontal_difference > 0:
                current = self.east(current, 1)
            if horizontal_difference < 0:
                current = self.west(current, 1)
            if self.get_piece(current) is not None:
                is_blocked = True
        return is_blocked

    def clear_piece(self, position: str):
        for block in self._board:
            if block.position == position:
                block.clear_piece()


def move_is_possible(piece: Piece, board: Board, move: Tuple[str, str]) -> bool:
    match piece:
        case Pawn() as pawn:
            return (pawn_can_move(board, pawn, move)
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


def pawn_can_move(board: Board, piece: Pawn, move: Tuple[str, str]) -> bool:
    # TODO TODO TODO  fix this shit, oh my god please
    before = move[0]
    after = move[1]
    # First move, forward 1 or 2 spaces
    horizontal_difference, vertical_difference = calculate_xy_difference(move)
    if not piece.has_moved():
        # moving on the same column
        if is_possible_vertical_move(move):
            # different restrictions per team
            if piece.get_team() == "white":
                # TODO we're not taking a piece
                # if board.get_piece(after) is None:
                # check if we're moving no more than 2 places
                if 2 >= calculate_vertical_difference(before, after) >= 1:
                    # TODO MOVE somewhere outside of this function
                    piece.set_has_moved()  # TODO this should be called outside of this function too
                    return True
            if board.get_piece(before).get_team() == "black":
                # TODO we're not taking a piece
                # if board.get_piece(after) is None:
                if -2 <= calculate_vertical_difference(before, after) <= -1:
                    # TODO MOVE somewhere outside of this function
                    piece.set_has_moved()  # TODO this should be called outside of this function too
                    return True
        else:
            if board.get_piece(before).get_team().lower() == "white":
                # check vertical bounds, 1 because of white pieces' board orientation
                # we're moving 2 places
                if vertical_difference != 1:
                    return False
                # check horizontal bounds
                if horizontal_difference != 1 or horizontal_difference != -1:
                    if board.get_piece(after) is not None:
                        # TODO MOVE somewhere outside of this function
                        piece.set_has_moved()  # TODO this should be called outside of this function too
                        return True
            if board.get_piece(before).get_team() == "black":
                # check vertical bounds, -1 because of black pieces' board orientation
                if vertical_difference != -1:
                    return False
                # check horizontal bounds
                if horizontal_difference == 1 or horizontal_difference == -1:
                    if board.get_piece(after) is not None:
                        # TODO MOVE somewhere outside of this function
                        piece.set_has_moved()  # TODO this should be called outside of this function too
                        return True
                    if board.get_piece(after) is not None:
                        # TODO MOVE somewhere outside of this function
                        piece.set_has_moved()  # TODO this should be called outside of this function too
                        return True
    return False

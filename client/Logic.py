class Outcome():
    def __init__(self) -> None:
        pass

    def is_legal(self):
        pass

    # if the target square is available move to piece
    # moving into check? that's not allowed
    # then if target square is occupied, you are attacking!

    def is_check(self):
        pass

    # king is attacked and can move or block attack

    def is_checkmate(self):
        pass

    # if King is in check, has 0 available moves, and attack can't be blocked

    def is_stalemate(self):
        pass

    # current player has 0 available moves

    def is_draw(self):
        pass

    # player accepted player "draw" request

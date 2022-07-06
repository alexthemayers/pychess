from Board import *
from Player import *

p: dict = {'p1': {'name': "firstname lastname", 'side': "white"},
           'p2': {'name': "first-ish-name last-ish-name", 'side': "black"}
           }


def create_players_check_repr() -> bool:
    p: dict = {'p1': {'name': "firstname lastname", 'side': "white"}}
    p1 = Player(p['p1']['name'], p['p1']['side'])
    if str(p1) == f"{p['p1']['name']}\t=>\t{p['p1']['side']}":
        return True
    else:
        return False


def printable_text_board() -> bool:
    board_str: str = str(BoardHelper().printable_board("text"))
    test_str: str = """a8(1,8)	b8(2,8)	c8(3,8)	d8(4,8)	e8(5,8)	f8(6,8)	g8(7,8)	h8(8,8)

a7(1,7)	b7(2,7)	c7(3,7)	d7(4,7)	e7(5,7)	f7(6,7)	g7(7,7)	h7(8,7)

a6(1,6)	b6(2,6)	c6(3,6)	d6(4,6)	e6(5,6)	f6(6,6)	g6(7,6)	h6(8,6)

a5(1,5)	b5(2,5)	c5(3,5)	d5(4,5)	e5(5,5)	f5(6,5)	g5(7,5)	h5(8,5)

a4(1,4)	b4(2,4)	c4(3,4)	d4(4,4)	e4(5,4)	f4(6,4)	g4(7,4)	h4(8,4)

a3(1,3)	b3(2,3)	c3(3,3)	d3(4,3)	e3(5,3)	f3(6,3)	g3(7,3)	h3(8,3)

a2(1,2)	b2(2,2)	c2(3,2)	d2(4,2)	e2(5,2)	f2(6,2)	g2(7,2)	h2(8,2)

a1(1,1)	b1(2,1)	c1(3,1)	d1(4,1)	e1(5,1)	f1(6,1)	g1(7,1)	h1(8,1)

"""
    if board_str == test_str:
        return True
    else:
        return False


def run_tests() -> None:
    if create_players_check_repr():  # add new if block for every test
        print("PASSED: create_players_check_repr()")
    else:
        print("FAILED: create_players_check_repr()")

    if printable_text_board():
        print("PASSED: printable_text_board()")
    else:
        print("FAILED: printable_text_board()")


if __name__ == "__main__":
    run_tests()

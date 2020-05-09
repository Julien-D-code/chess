#!/usr/bin/python3

import chess_package.objects.board.board as bd
from chess_package.objects.board.instancie.square import *
from pprint import pprint

def main():
    pl = bd.Board()
    print(type(pl))
    for u in pl.getBoard():
        print(pl.getBoard()[u].getSquare())


if __name__ == "__main__":
    main()

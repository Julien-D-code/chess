#!/usr/bin/python3
import chess_package.objects.plateau.board as bd

def main():
    pl = bd.Board()
    print(type(pl))
    print(pl.board["A1"].piece.getColor())

    # pl.board["A1"].piece.setColor()
    # print(pl.board["A1"].piece.type)

if __name__ == "__main__":
    main()

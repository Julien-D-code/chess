#!/usr/bin/python3
import chess_package.objects.board.board as bd

def main():
    pl = bd.Board()
    print(type(pl))
    print(pl.board["A1"].piece.getColor())
    print(pl.board["A1"].piece.getMouv())
    print(pl.board["A1"].piece.getNb())
    print(pl.board["A1"].piece.addNb())
    print(pl.board["A1"].piece.getNb())
    print(pl.board["A1"].piece.getType())
    # pl.board["A1"].piece.setColor()
    # print(pl.board["A1"].piece.type)

if __name__ == "__main__":
    main()

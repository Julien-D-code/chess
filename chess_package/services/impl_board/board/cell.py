from ....static.PIECES import Labels_Pieces
from ....objects.board.instancie.square import *
from ....objects.pieces.instancie.bishop import *
from ....objects.pieces.instancie.king import *
from ....objects.pieces.instancie.knight import *
from ....objects.pieces.instancie.pawn import *
from ....objects.pieces.instancie.queen import *
from ....objects.pieces.instancie.tower import *

#Main function of this file
def cell(cell_id, color_cell, color_piece):

    #If line egale to 1 or 8 then it's a figure piece like tower or anything like that, according to the chess game
    if cell_id[1] == '1' or cell_id[1] == '8':
        board = figure(cell_id, color_cell, color_piece)

    #If line egale to 2 or 7 then it's a pawn according to the chess game
    elif cell_id[1] == '2' or cell_id[1] == '7':
        board = pawn(cell_id, color_cell, color_piece)

    #Else we have a cell with no piece
    else:
        board = empty_cell(cell_id, color_cell)

    return board

#We have cell color and piece color so we just need to set the appropriate type of piece
def figure(cell_id, color_cell, color_piece):

    # Tower according to the chess game
    if cell_id[0] in ['A','H']:
        return{cell_id:Square(color=color_cell,\
        piece=Tower(color=color_piece, type=Labels_Pieces.TOWER), id=cell_id)}

    # Knight according to the chess game
    elif cell_id[0] in ['B','G']:
        return {cell_id:Square(color=color_cell,\
        piece=Knight(color=color_piece, type=Labels_Pieces.KNIGHT), id=cell_id)}

    #....
    elif cell_id[0] in ['C','F']:
        return {cell_id:Square(color=color_cell,\
        piece=Bishop(color=color_piece, type=Labels_Pieces.BISHOP), id=cell_id)}

    elif cell_id[0] == 'D':
        return {cell_id:Square(color=color_cell,\
        piece=Queen(color=color_piece, type=Labels_Pieces.QUEEN), id=cell_id)}

    else:
        return {cell_id:Square(color=color_cell,\
        piece=King(color=color_piece, type=Labels_Pieces.KING), id=cell_id)}

#Same logical as before
def pawn(cell_id, color_cell, color_piece):
    return {cell_id:Square(color=color_cell,\
    piece=Pawn(color=color_piece, type=Labels_Pieces.PAWN), id=cell_id)}

#Empty cell, no piece
def empty_cell(cell_id, color_cell):
    return {cell_id:Square(color=color_cell, id=cell_id)}

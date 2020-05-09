from ...static.PIECES import Labels_Pieces
from ...static.COLORS import Labels_Colors
from .mouv_init.mouv_init import *

# I see movement like that :
#
#                             Cartesian plane
#
#                                    y
#                                    |
#                                    |
#                                    |
#                                    | [0,1] [1,1]
#                                    | [0,0] [1,0]
#                  ------------------------------------- x
#                        [-1,0] [0,0]|
#                      [-1,-1] [0,-1]|
#                                    |
#                                    |
#                                    |
#
# We need to set a relative coordinate for all square from a selected piece being like an origin

# Set a multiplicator coeficient like 1 or -1 depending to the piece color
def init(piece):

    mult = 1 if piece.getColor() == Labels_Colors.WHITE else -1
    return mult

# Switch depending to the type piece
def impl_mouv(piece):
    # Call init() function
    mult = init(piece)

    switch = {
        Labels_Pieces.BISHOP:bishop(mult),
        Labels_Pieces.KING:king(mult),
        Labels_Pieces.KNIGHT:knight(mult),
        Labels_Pieces.PAWN:pawn(mult),
        Labels_Pieces.QUEEN:queen(mult),
        Labels_Pieces.TOWER:tower(mult)
    }

    # Get key from dic
    mouv = switch.get(piece.getType())
    return mouv

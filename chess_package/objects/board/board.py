from .instancie.square import *
from ...services.impl_board.impl_board import *
from ...static.COLORS import Labels_Colors
from ...static.PIECES import Labels_Pieces
from ..pieces.instancie.bishop import *
from ..pieces.instancie.king import *
from ..pieces.instancie.knight import *
from ..pieces.instancie.pawn import *
from ..pieces.instancie.queen import *
from ..pieces.instancie.tower import *

class Board():

    def __init__(self):

        self.board = {
            "A1":Square(color=Labels_Colors.WHITE,\
            piece=Bishop(color=Labels_Colors.WHITE, type=Labels_Pieces.BISHOP), id="A1"),
        }

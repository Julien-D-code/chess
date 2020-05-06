from .instancie.square import *
from ...services.impl_board.impl_board import *
from ...static.COLORS import *
from ..pieces.instancie.bishop import *
from ..pieces.instancie.king import *
from ..pieces.instancie.knight import *
from ..pieces.instancie.pawn import *
from ..pieces.instancie.queen import *
from ..pieces.instancie.tower import *

class Board():

    def __init__(self):
        self.board = {}
        # self.board = {
        #
        # "A1":Square(color=Colors.WHITE_COLOR,\
        # piece=Bishop(color=Colors.WHITE_COLOR, type='BISHOP'), id="A1"),
        #
        # "A1":Square(color=Colors.WHITE_COLOR,\
        # piece=Bishop(color=Colors.WHITE_COLOR, type='BISHOP'), id="A1"),
        #
        # "A1":Square(color=Colors.WHITE_COLOR,\
        # piece=Bishop(color=Colors.WHITE_COLOR, type='BISHOP'), id="A1"),
        #
        # "A1":Square(color=Colors.WHITE_COLOR,\
        # piece=Bishop(color=Colors.WHITE_COLOR, type='BISHOP'), id="A1"),
        #
        # "A1":Square(color=Colors.WHITE_COLOR,\
        # piece=Bishop(color=Colors.WHITE_COLOR, type='BISHOP'), id="A1"),
        #
        # }

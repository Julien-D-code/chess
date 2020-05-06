from ..pieces import *

class Pawn(Pieces):

    def __init__(self, color='None', type='None'):
        super().__init__(color, type)
        self._special_move = []

    def getSpecMouve(self):
        return(self._special_move)

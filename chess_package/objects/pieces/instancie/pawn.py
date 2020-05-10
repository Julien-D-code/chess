from ..pieces import *

class Pawn(Pieces):

    def __init__(self, color=None, type=None, special=True):
        super().__init__(color, type, special)
        self._special_move = []

    def getSpecMouve(self):
        return self._mouvement['special']

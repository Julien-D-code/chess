from ..pieces import *

class Tower(Pieces):

    def __init__(self, color='None', type='None'):
        super().__init__(color, type)
        self._special_move = []
        mouv = {'basic':[], 'first_mouv':[]}

    def getSpecMouve(self):
        return(self._special_move)

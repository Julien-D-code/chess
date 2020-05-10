from ..pieces import Pieces

class King(Pieces):

    def __init__(self, color=None, type=None, special=True):
        super().__init__(color, type, special)

    def getSpecMouve(self):
        return self._mouvement['special']

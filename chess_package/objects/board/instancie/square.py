from ...pieces.pieces import *

class Square():

    def __init__(self, color=None, piece=None, id=None):
        self._color = color
        self.piece = piece
        self._id = id

    def getColor(self):
        return(self._color)

    def getId(self):
        return(self._id)

    # Just for seeing if all is allright
    def getSquare(self):
        if self.piece != None:
            buf = str(self._id)+"\t"+str(self._color)+"\t"+str(self.piece.getType())+"\t"+str(self.piece.getColor())
        else:
            buf = str(self._id)+"\t"+str(self._color)+"\t"+str(self.piece)
        return buf

    def setSquare(self, color=None, piece=None, id=None):
        super().__init__(color=None, piece=None, id=None)

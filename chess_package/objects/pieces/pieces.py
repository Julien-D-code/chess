from abc import ABC, abstractmethod

class Pieces(ABC):

    @abstractmethod
    def __init__(self, color='None', type='None', nb=0, mouvement={'basic':[], 'first':[]}):
        self._color = color
        self._mouvement = mouvement
        self.nb = nb
        self.type = type

    def getColor(self):
        return(self._color)

    def setColor(self,value):
        self._color = value

    def getType(self):
        return(self.type)

    def setType(self,value):
        self.type = value

    def getMouv(self):
        return(self._mouvement)

    def setMouv(self, value):
        return(self._mouvement)

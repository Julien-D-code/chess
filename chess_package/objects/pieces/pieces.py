from abc import ABC, abstractmethod

class Pieces(ABC):
# Commentaire test
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

    def getMouv(self):
        return(self._mouvement)

    def setMouv(self, value):
        return(self._mouvement)

    def getNb(self):
        return(self.nb)

    def addNb(self):
        self.nb += 1

    def getType(self):
        return(self.type)

    def setType(self,value):
        self.type = value

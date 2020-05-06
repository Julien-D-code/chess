from abc import ABC, abstractmethod

class Pieces(ABC):

    @abstractmethod
    def __init__(self, color='None', type='None', mouvement=[]):
        self._color = color
        self._type = type
        self._mouvement = mouvement

    def getColor(self):
        return(self._color)

    def setColor(self,value):
        self._color = value

    def getType(self):
        return(self._type)

    def setType(self,value):
        self._type = value

    def getMouv(self):
        return(self._mouvement)

    def setMouv(self, value):
        return(self._mouvement)

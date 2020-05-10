from abc import ABC, abstractmethod
from ...services.impl_mouv_init.impl_mouv_init import impl_mouv

class Pieces(ABC):

    @abstractmethod
    def __init__(self, color=None, type=None, special=False, nb=0, mouvement=None):
        self._color = color
        self._type = type
        self._mouvement = self.setMouv(self)
        self.nb = nb
        self.special = special

    def getColor(self):
        return self._color

    def setColor(self,value):
        self._color = value

    def getType(self):
        return self._type

    def setType(self,value):
        self._type = value

    def getMouv(self):
        return self._mouvement['init']

    def setMouv(self, value):
        mouv = impl_mouv(self)
        return mouv

    def getNb(self):
        return self.nb

    def addNb(self):
        self.nb += 1

    def iSpecial(self):
        return self.special

    def setSpecial(self,value):
        self.special = value

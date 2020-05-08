from abc import ABC, abstractmethod
from ...services.impl_mouv_init.impl_mouv_init import impl_mouv

class Pieces(ABC):
# Commentaire test
    @abstractmethod
    def __init__(self, color='None', type='None', nb=0, mouvement=None):
        self._color = color
        self._type = type
        self._mouvement = self.setMouv(self)
        self.nb = nb

    def getColor(self):
        return(self._color)

    def setColor(self,value):
        self._color = value

    def getType(self):
        return(self._type)

    def setType(self,value):
        self._type = value

    def getMouv(self):
        # TO FUNCTION
        # if n == 0:
        #     mouv = self._mouvement['basic'].extend(self._mouvement['first'])
        # else:
        #     mouv = self._mouvement['basic']
        return(self._mouvement)

    def setMouv(self, value):
        mouv = impl_mouv(self)
        return(mouv)

    def getNb(self):
        return(self.nb)

    def addNb(self):
        self.nb += 1

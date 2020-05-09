from ...services.impl_board.impl_board import setBoard

class Board():

    def __init__(self):
        self.board = setBoard()

    def getBoard(self):
        return(self.board)

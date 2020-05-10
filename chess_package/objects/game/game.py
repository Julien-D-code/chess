from ..board.board import Board

class Game(Board):

    def __init__(self, player=None):
        self.board = super()__init__()
        self._player_1 = player[0]
        self._player_2 = player[1]

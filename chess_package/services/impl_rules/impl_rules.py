from ...static.PIECES import Labels_Pieces

# BEFORE SETTING RULES WE NEED TO DEFINE RELATIVE MOVE

#My idea is to fragment the rules for the pieces need. In fact the roque or "en passant"
#rules need to be verify if the piece is like a king or a pawn. it's the purpose of switch
#All of these rules are define in the directory rules.
#We need the piece (for the type) the board for checking the state of the game and verify
#if the king are still alive in the next move.
def rules(board, piece, possible_path):
    #Switch pawn or king else other
    switch = {
        Labels_Pieces.PAWN:pawn(board, piece, possible_path)
        Labels_Pieces.KING:king(board, piece, possible_path)
    }

    possible_path = switch.get(piece.getType(), other(board, piece, possible_path))
    return possible_path

def pawn(board, piece, possible_path):

    possible_path = en_passant(board, piece, possible_path)
    possible_path = echeque(board, piece, possible_path)
    return possible_path

def king(board, piece, possible_path):

    possible_path = roque(board, piece, possible_path)
    possible_path = echeque(board, piece, possible_path)
    return possible_path

def other(board, piece, possible_path):

    possible_path = echeque(board, piece, possible_path)
    return possible_path

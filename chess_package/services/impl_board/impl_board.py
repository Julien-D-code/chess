from ...static.COLORS import Labels_Colors
from .board.cell import cell

# I saw the board like x square and for each square we need to define a color
# attribut, so when i'm looking the chess board i see a patern like that:
#
# column   a b c d e
# row_1    0 1 0 1 0
# row_2    1 0 1 0 1
# row_3    0 1 0 1 0
#
# when the value is like 0 then it's black else is WHITE

def setBoard():

    #Defining an empty new dictionary for adding new cell to the board
    board = {}

    #Code column
    column = {
        'A':0,
        'B':1,
        'C':0,
        'D':1,
        'E':0,
        'F':1,
        'G':0,
        'H':1
    }

    #Code row
    row = {
        '1':0,
        '2':1,
        '3':0,
        '4':1,
        '5':0,
        '6':1,
        '7':0,
        '8':1
    }

    #Defining a new dictionary for color value
    color = {"1":Labels_Colors.WHITE, "0":Labels_Colors.BLACK}

    #Browsing column and row dictionary
    for col in column:
        for row_ in row:

            #Seting the code value
            case_value = column[col] + row[row_]

            #If the code value is like 2 then we need to set to 0 BLACK color
            # refering to the previous tab :
            #
            # if we take row['2'] and col['B'] we have 1+1=2 but in fact we need 0
            # for setting Black color. So black = 0 or 2
            #
            # column   a b c d e
            # row_1    0 1 0 1 0
            # row_2    1 [0] 1 0 1
            # row_3    0 1 0 1 0
            #
            # we can have 1+1
            case_value = case_value if case_value != 2 else 0

            #Case Id like "A1" or anything like that
            case_id = col+row_

            #We need to set a color piece, that's pretty simple if we have row 1 or 2
            #then it's White else it's Black
            color_piece = Labels_Colors.WHITE if int(row_) < 5 else Labels_Colors.BLACK

            #Updating board we call a cell function from board/cell.py
            board.update(cell(case_id, color[str(case_value)], color_piece))

    #Then our board is initialize
    return board

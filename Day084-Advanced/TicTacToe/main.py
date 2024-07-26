from player import Player

"""Tic Tac Toe Project"""

# Print Board

"-------|-------|-------"
"   A   |   B   |   C   "
"-------|-------|-------"
"   D   |   E   |   F   "
"-------|-------|-------"
"   G   |   H   |   I   "
"-------|-------|-------"

boardArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']


def displayBoard():
    # init vars
    horizontal = "-------"
    vertical = "|"
    space = "       "
    isSpace = False


    for row in range(7):
        for i in range(3):
            print(space, end="") if isSpace else print(horizontal, end="")
            if i != 2: print(vertical, end="")
        print()  # Move to the next line after printing the row
        isSpace = not isSpace  # Toggle the value of isSpace at the end of each row iteration


displayBoard()

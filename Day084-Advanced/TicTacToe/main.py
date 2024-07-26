"""Tic Tac Toe Project"""

# Print Board

"-------|-------|-------"
"   A   |   B   |   C   "
"-------|-------|-------"
"   D   |   E   |   F   "
"-------|-------|-------"
"   G   |   H   |   I   "
"-------|-------|-------"

# Set Walls - Wunderbar :)
def setRP(isSpace):
    horizontal = "-------"
    vertical = "|"
    space = "       "

    for i in range(3):
        print(space, end="") if isSpace else print(horizontal, end="")
        if i != 2: print(vertical, end="")
    print()  # Move to the next line after printing the row

def printBoard():

    isSpace = False  # Initial state

    for row in range(7):
        setRP(isSpace)
        isSpace = not isSpace  # Toggle the value of isSpace at the end of each row iteration


printBoard()

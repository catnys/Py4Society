from box import Box

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
empty_board = [' '] * 9


def displayBoard(boardArray):
    # init vars
    horizontal = "-------"
    vertical = "|"
    index = 0
    isSpace = False

    for row in range(7):
        for i in range(3):
            if isSpace:
                space = f"   {boardArray[index]}   "
                print(space, end="")
                index += 1
            else:
                print(horizontal, end="")
            if i != 2: print(vertical, end="")
        print()  # Move to the next line after printing the row

        isSpace = not isSpace  # Toggle the value of isSpace at the end of each row iteration


displayBoard(boardArray)

from box import Box
from player import Player

"""Tic Tac Toe Project"""

# Print Board

"-------|-------|-------"
"   1   |   2   |   3   "
"-------|-------|-------"
"   4   |   5   |   6   "
"-------|-------|-------"
"   7   |   8   |   9   "
"-------|-------|-------"


boardArrayNumeric = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
empty_board = [' '] * 9



def initBoardArray():
    boardArray = []
    for i in range(9):
        square = Box(" ",True)
        boardArray.append(square)
    return boardArray


def updateBoardArray(boardArray, player: Player, index: int):
    for i in range(9):
        if index == i:
            boardArray[i].letter = player.getSymbol()


def displayBoard(boardArray):
    # init vars
    horizontal = "-------"
    vertical = "|"
    index = 0
    isSpace = False

    for row in range(7):
        for i in range(3):
            if isSpace:
                space = f"   { boardArray[index].getLetter() if boardArray[index].getLetter() != ' ' else boardArrayNumeric[index]}   "
                print(space, end="")
                index += 1
            else:
                print(horizontal, end="")
            if i != 2: print(vertical, end="")
        print()  # Move to the next line after printing the row

        isSpace = not isSpace  # Toggle the value of isSpace at the end of each row iteration

p1 = Player("X")
p2 = Player("O")

boardArray = initBoardArray()
updateBoardArray(boardArray, p1, 1)
updateBoardArray(boardArray, p2, 5)
displayBoard(boardArray)

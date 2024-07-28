from box import Box
from player import Player
import os

"""Tic Tac Toe Project"""

# Print Board

"-------|-------|-------"
"   1   |   2   |   3   "
"-------|-------|-------"
"   4   |   5   |   6   "
"-------|-------|-------"
"   7   |   8   |   9   "
"-------|-------|-------"


def initBoardArray():
    boardArray = []
    for i in range(9):
        square = Box(letter=str(i + 1))
        boardArray.append(square)
    return boardArray


def reserveIndex(boardArray, player: Player, index: int):
    for i in range(9):
        if index == i:
            boardArray[i].setLetter(player.getSymbol())


def displayBoard(boardArray):
    # init vars
    horizontal = "-------"
    vertical = "|"
    index = 0
    isSpace = False

    for row in range(7):
        for i in range(3):
            if isSpace:
                space = f"   {boardArray[index].getLetter()}   "
                print(space, end="")
                index += 1
            else:
                print(horizontal, end="")
            if i != 2: print(vertical, end="")
        print()  # Move to the next line after printing the row

        isSpace = not isSpace  # Toggle the value of isSpace at the end of each row iteration


def hasEmptyPlaces(boardArray):
    for box in boardArray:
        if box.getLetter().isnumeric():  # Check if the letter is numeric (i.e., an unmarked space)
            return True  # Return True as soon as an empty place is found
    return False  # Return False if no empty places were found


def playGame(player1: Player, player2: Player,boardArray):
    """Display the game menu"""
    GameOver = False


    while not GameOver:
        displayBoard(boardArray)
        # For each iteration

        occupiedBlock = input(f"What block would you like to mark? (as {player1.getSymbol()}): ")

        os.system('cls' if os.name == 'nt' else 'clear')


p1 = Player("X")
p2 = Player("O")

boardArray = initBoardArray()
print("----")
for i in range(9):
    print(boardArray[i].getLetter())
print("----")
reserveIndex(boardArray, p1, 1)
reserveIndex(boardArray, p2, 5)
displayBoard(boardArray)

print(boardArray[1].getLetter().isnumeric())

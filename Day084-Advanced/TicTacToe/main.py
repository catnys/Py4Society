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


def checkWin(currentPlayer,boardArray):
    """Check if the current player has won."""
    # Define winning conditions
    winConditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    symbol = currentPlayer.getSymbol()
    return any(all(boardArray[i].getLetter() == symbol for i in condition) for condition in winConditions)


def playGame(player1: Player, player2: Player, boardArray):
    """Play the Tic Tac Toe game."""
    gameOver = False
    currentPlayer = player1  # Start with player 1

    while not gameOver:
        displayBoard(boardArray)
        print(f"Current player: {currentPlayer.getSymbol()}")

        # Check if there are still empty places on the board
        if not hasEmptyPlaces(boardArray):
            print("The board is full. Game Over.")
            gameOver = True
            break  # End the game if the board is full

        try:
            occupiedBlock = int(input(f"What block would you like to mark? (as {currentPlayer.getSymbol()}): ")) - 1
            if occupiedBlock < 0 or occupiedBlock > 8 or not boardArray[occupiedBlock].getLetter().isnumeric():
                raise ValueError("Invalid move")
            reserveIndex(boardArray, currentPlayer, occupiedBlock)
            if checkWin(currentPlayer,boardArray):
                print(f"{currentPlayer.getSymbol()} wins!")
                gameOver = True
                break
        except ValueError as e:
            print(e)
            continue

        # Switch players
        currentPlayer = player2 if currentPlayer == player1 else player1
        os.


def main():
    p1 = Player("X")
    p2 = Player("O")

    boardArray = initBoardArray()

    """
    # Example moves to demonstrate functionality
    reserveIndex(boardArray, p1, 1)
    reserveIndex(boardArray, p2, 5)
    """

    playGame(p1, p2, boardArray)


if __name__ == "__main__":
    main()

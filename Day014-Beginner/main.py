import os
import random
from user import User
from art import logo, vs
from gamedata import data


def displayGameData(list):
    for item in list:
        print(item)


def pickRandomData():
    element = random.choice(data)
    return element


def createUser():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    return User(username, password)


def saveUser(user, filename):
    """Save or update a user's score in credentials.txt."""
    mode = 'w' # set more to write initially
    # Check if the file exists
    if os.path.exists(filename):
        # file exist, so open w/ append mode as 'a'
        # set the mode as 'a'
        mode = 'a'

    with open(filename, mode) as file:
        file.write(str(user) + "\n")



def playGame():
    """Main function to handle the game operations."""
    isOver = False
    score = 0
    while not isOver:
        print(logo)
        questA = pickRandomData()
        questB = pickRandomData()
        print(f"Compare A : {questA['name']}, a {questA['description']}, from {questA['country']}")
        print(vs)
        print(f"Agains B: {questB['name']}, a {questB['description']}, from {questB['country']}")
        answer = str(input("Who has more followers? Type 'A' or 'B':"))

        if questA['follower_count'] > questB['follower_count']:
            if answer == 'A':
                score += 1
            else:
                score -= 1
        else:
            if answer == 'B':
                score += 1
            else:
                score -= 1

        if score < 0:
            print(f"Sorry {questA['name']}, you lose {questB['name']}")
            isOver = True
        else:
            print(f"\nYour score is {score}\n")


def main():
    fileName = "credentials.txt"
    user1 = User("Kimberly", "K1mberly3")
    print(user1)
    saveUser(user1, fileName)

    """
    while True:
        playGame()
        if input("Do you want to play another game ? Type 'y' for yes, 'n' for no: ").lower() != 'y':
            break
    """


if __name__ == '__main__':
    main()

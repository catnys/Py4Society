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


def saveUser(user, filename, userlist):
    """Save user to the credentials.txt file"""
    mode = 'w' # set more to write initially
    # Check if the file exists
    if os.path.exists(filename):
        # file exist, so open w/ append mode as 'a'
        # set the mode as 'a'
        mode = 'a'

    with open(filename, mode) as file:
        for person in userlist:
            if user.username == person.username:
                file.write(str(user) + "\n")
        else:
            print("User already exists")


def loadUser(filename):
    """Load the user from credentials.txt"""

    # Initialize an empty dictionary to store the user data
    users = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Split the line into parts: username, password, and score
                parts = line.split(',')
                username = parts[0].strip()
                password = parts[1]
                score = int(parts[2])

                # Add the user data to the dictionary
                users.append(User(username, password, score))
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return users


def printUser(users):
    """Print the users list"""
    for user in users:
        print(f"{user.username}: {user.password} - {user.score}")

def isUserExist(filename,userlist,username):
    """Check whether a username exists"""

    for user in userlist:
        if user.username == username:
            return True
    return False

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

    """user1 = User("Kimberly", "password")
    print(user1)
    saveUser(user1, fileName)
    
    saveUser(User("John", "Doe"), fileName)
    saveUser(User("Avis", "123123."),fileName)
    """

    users = loadUser(fileName)
    printUser(users)
    saveUser(User("Kevin", "asd123 "), fileName,users)

    print(isUserExist(fileName,users, "Avis"))

    """
    while True:
        playGame()
        if input("Do you want to play another game ? Type 'y' for yes, 'n' for no: ").lower() != 'y':
            break
    """


if __name__ == '__main__':
    main()

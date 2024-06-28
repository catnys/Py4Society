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
    mode = 'w'  # set more to write initially
    # Check if the file exists
    if os.path.exists(filename):
        # file exist, so open w/ append mode as 'a'
        # set the mode as 'a'
        mode = 'a'
    if not findUserByName(userlist, user.username):
        with open(filename, mode) as file:
            file.write(str(user) + "\n")


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


def updateUsers(filename, users):
    """Update the user in the credentials.txt file"""
    with open(filename, 'w') as file:
        for user in users:
            file.write(str(user) + "\n")


def printUser(users):
    """Print the users list"""
    for user in users:
        print(f"{user.username}: {user.password} - {user.score}")


def isUserExist(filename, userlist, username):
    """Check whether a username exists"""

    for user in userlist:
        if user.username == username:
            return True
    return False


def findUserByName(users, username):
    for user in users:
        if user.username == username:
            return user
    return None  # Return None if no user is found with the given username


def playGame(user):
    """Main function to handle the game operations."""

    isOver = False
    score = 0
    lives = 2
    print(logo)

    while not isOver:

        questA = pickRandomData()
        questB = pickRandomData()
        print(f"score: {score}")
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
                lives -= 1

        if lives == 0:
            print(f"\n\n\nSorry {user.username}, you lose :(")
            isOver = True
        elif answer == 'Q':
            print(f"\nYou have just quit!\n")
            isOver = True

    print(f"score : {score} ")
    user.score += score


def registerUser(filename, userlist):
    print("Registration")
    username = input("Choose a username: ")
    if findUserByName(userlist, username):
        print("Username already taken. Please try a different username.")
        return None
    password = input("Choose a password: ")
    newUser = User(username, password, 0)
    saveUser(newUser, filename, userlist)
    userlist.append(newUser)
    return newUser


def loginUser(users):
    count = 3
    print("Login")
    while count != 0:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = findUserByName(users, username)
        if user and user.password == password:
            print("Login successful!")
            return user
        else:
            count -= 1
            print(f"Invalid username or password. Please try again. Remaining try is {count}")

    return None


def main():
    filename = "credentials.txt"

    # Load existing users
    users = loadUser(filename)

    # Initial menu for login or registration
    while True:
        choice = input("Do you want to [login] (l) or [register] (r)? ")
        if choice.lower() == 'login' or choice.lower() == 'l':
            user = loginUser(users)
            if user:
                print("-------------------------")
                print(f"Welcome! {user.username}")
                print("-------------------------")
                break
        elif choice.lower() == 'register' or choice.lower() == 'r':
            user = registerUser(filename, users)
            if user:
                print("-------------------------")
                print("Thank you for registering!")
                print("-------------------------")
                break
        else:
            print("Please enter 'login' or 'register'.")

    print(user)
    # Play the game after successful login or registration
    while True:
        playGame(user)
        if input("Do you want to play another game? Type 'y' for yes, 'n' for no: ").lower() != 'y':
            break

    printUser(users)
    # Save the user's new score
    updateUsers(filename, users)


if __name__ == '__main__':
    main()

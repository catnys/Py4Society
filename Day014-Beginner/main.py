import random
from art import logo
from gamedata import data


def displayGameData(list):
    for item in list:
        print(item)


def displayLogo():
    """Displays the logo."""
    print(logo)


def pickRandomData():

    element = random.choice(data)
    quest = f"{element['name']}, a {element['description']}, from {element['country']}"
    return quest


def displayQuest()


def main():
    displayLogo()
    displayGameData(data)
    print(f"Compare A : {pickRandomData()}")




if __name__ == '__main__':
    main()

import random
from art import logo, vs
from gamedata import data


def displayGameData(list):
    for item in list:
        print(item)


def pickRandomData():
    element = random.choice(data)
    quest = f"{element['name']}, a {element['description']}, from {element['country']}"
    return quest



def playGame():
    """Main function to handle the game operations."""
    isOver = False
    score = 0
    while not isOver:
        print(logo)
        questA = pickRandomData()
        questB = pickRandomData()
        print(f"Compare A : {questA}")
        print(vs)
        print(f"Agains B: {questB}")
        answer = input("Who has more followers? Type 'A' or 'B':")

        if questA['follower_count'] > questB['follower_count']:
            if answer == 'A':
                score += 1
        else:
            if answer == 'B':
                score += 1




def main():
    while True:
        playGame()
        if input("Do you want to play another game ? Type 'y' for yes, 'n' for no: ").lower() != 'y':
            break


if __name__ == '__main__':
    main()

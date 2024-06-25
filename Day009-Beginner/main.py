import art
import os

# Define global people dictionary
people = []

def showLogo():
    print(art.logo)

def displayDictionary(people):
    for person in people:
        print(person)


def getUserInfo():

    others = True

    while others == True:
        name = str(input("What is your name? "))
        bid = int(input("What is your bid? $"))

        print("Are there any other bidders ? Type 'yes' or 'no'")
        others = True if str(input()).lower() == 'yes' else False

        print(f"{name} has {bid} bid. You have {others} others.")
        myDictionary = {'name': name, 'bid': bid}
        people.append(myDictionary)
        os.system('clear')


def findMax(people):
    maxBid = 0
    for person in people:
        if person['bid'] > maxBid:
            maxBid = person['bid']
            maxName = person['name']

    print(f"{maxName} has the highest bid which is ${maxBid}.")




def main():
    # showLogo()
    # getUserInfo()
    people = [
        {'name': "Alice", 'bid': 100},
        {'name': "Bob", 'bid': 200},
        {'name': "John", 'bid': 300},
        {'name': "Sarah", 'bid': 800},
        {'name': "David", 'bid': 400},
    ]
    # print(people)
    findMax(people)



if __name__ == "__main__":
    main()

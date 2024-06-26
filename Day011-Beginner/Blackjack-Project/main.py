############### Blackjack Project #####################
import random
# import os
from art import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################


def getRandomCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
userCards = []
computerCards = []


def calculateScore(cards):
    score = 0
    for card in cards:
        score += card

    if score == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    return int(score)

def compare(userScore, computerScore):
    if userScore < 21:
        if userScore == 0 or userScore > computerScore:
            print("You win!")
    else:
        print("You lose!")


def makeEmptyLists(userCards, computerCards):
    userCards.clear()
    computerCards.clear()

def main():
    isOver = False

    while True:
        print(logo)
        print("Welcome to Blackjack Game!")

        # give user and computer 2 random cards first
        userCards.append(getRandomCard())
        userCards.append(getRandomCard())
        computerCards.append(getRandomCard())
        computerCards.append(getRandomCard())
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)



        while not isOver:
            print(f" Your cards: {userCards}, current score: {calculateScore(userCards)}")
            print(f"Computer cards: {computerCards[0]}")

            # Check for Blackjack or score over 21
            if computerScore >= 21 or userScore >= 21:
                isOver = True
            else:
                # User decides to get another card
                if input("Type 'y' to get another card, any other key to pass: ").lower() == 'y':
                    randomCard = getRandomCard()
                    userCards.append(randomCard)
                    userScore += randomCard
                else:
                    isOver = True


            if computerScore < 17:
                randomCard = getRandomCard()
                computerCards.append(randomCard)
                computerScore += randomCard

        print(f"Your final score: {calculateScore(userCards)} and computer final score: {calculateScore(computerCards)}")
        compare(userScore, computerScore)
        makeEmptyLists(userCards, computerCards)
        if input("Would you like to play again? (y or n): ").lower() == 'y':
            isOver = False
            # os.system("clear") # for windows --> "cls"
        else:
            break



if __name__ == '__main__':
    main()

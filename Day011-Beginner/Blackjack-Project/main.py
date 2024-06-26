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

userCards = []
computerCards = []

def getRandomCard():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)




def calculateScore(cards):
    """Calculates and returns the score considering Blackjack rules."""
    score = sum(cards)
    # Adjust for the Ace being 1 or 11
    if 11 in cards and score > 21:
        return score - 10
    return score


def compare(userScore, computerScore):
    """Compares user and computer scores and prints the outcome."""
    if userScore > 21:
        print("Bust! You lose.")
    elif computerScore > 21 or userScore > computerScore:
        print("You win!")
    elif userScore < computerScore:
        print("You lose!")
    else:
        print("It's a tie!")


def makeEmptyLists(userCards, computerCards):
    userCards.clear()
    computerCards.clear()



def playBlackjack():
    """Main function to handle the game operations."""
    print(logo)
    print("Welcome to Blackjack Game!")
    userCards, computerCards = [], []
    gameOver = False

    userCards.extend([getRandomCard(), getRandomCard()])
    computerCards.extend([getRandomCard(), getRandomCard()])

    while not gameOver:
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        print(f"Your cards: {userCards}, score: {userScore}")
        print(f"Computer's first card: {computerCards[0]}")

        # Check for Blackjack or score over 21
        if computerScore >= 21 or userScore >= 21:
            gameOver = True
        else:
            # User decides to get another card
            if input("Type 'y' to get another card, any other key to pass: ").lower() == 'y':
                userCards.append(getRandomCard())
            else:
                gameOver = True

        if computerScore < 17:
            computerCards.append(getRandomCard())

        print("--------------------")

    print(f"Computer's final hand: {computerCards}, final score: {computerScore}")
    compare(userScore, computerScore)



def main():
    while True:
        playBlackjack()
        if input("Do you want to play another game of Blackjack? Type 'y' for yes, 'n' for no: ").lower() != 'y':
            break



if __name__ == '__main__':
    main()

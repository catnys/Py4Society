# Blackjack Game Project

Welcome to the Blackjack Game Project! This project simulates a simple game of Blackjack, where the player can play against the computer, which acts as the dealer. The game is designed with basic rules and is easy to play from the command line.

## Project Description

The Blackjack game is developed in Python and can be run directly from the command line. The game follows the traditional rules of Blackjack, also known as 21. Here are the key features:

- **Unlimited Deck Size:** The deck is considered to be unlimited; cards are randomly generated as needed without deck depletion.
- **Simple Card Values:** The Jack, Queen, and King are valued at 10. Aces can be 1 or 11, depending on the player's hand.
- **Dealer Rules:** The computer dealer follows a simple rule to hit until reaching a score of at least 17.

## Setup and Execution

To run this project, you will need Python installed on your computer. No external libraries are required as the project uses built-in modules only.

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the game using Python:
   ```
   python main.py
   ```

## How to Play

- The game starts by dealing two cards to both the player and the dealer.
- The player sees both their cards and one of the dealer's cards.
- The player then chooses to hit (get another card) or stay (end their turn).
- The dealer's turn follows the player's turn. The dealer must hit if the score is below 17.
- The game ends when the player chooses to stay, exceeds 21 points, or obtains a Blackjack (21 points with the first two cards).
- Wins, losses, and ties are determined at the end of each round.

## Contributing

Contributions to the Blackjack Game Project are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Submit a pull request.

## TODO

- **Enhance AI Decision Making:** Improve the computer dealer's strategy to make gameplay more challenging.
- **Add Multiplayer Support:** Implement functionality for multiple players against the dealer.
- **Graphical User Interface (GUI):** Develop a simple GUI for the game to improve user interaction.
- **Advanced Game Features:** Implement betting systems and card counting features.

## License

This project is open-source and available under the MIT License.

Thank you for checking out the Blackjack Game Project. Enjoy playing!

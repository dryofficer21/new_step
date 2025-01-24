# Mini-Project 4: Vrai, Passe, Faux

This is a simple number guessing game implemented in Python. The game is called "Vrai, Passe, Faux" where the player has to guess a 4-digit secret number with unique digits. The game provides feedback for each guess to help the player deduce the secret number.

## Functionalities

1. **Generate Secret Number**:
    - The function `generate_secret_number()` generates a random 4-digit number with unique digits.

2. **Get Feedback**:
    - The function `get_feedback(secret, guess)` compares the player's guess with the secret number and provides feedback:
        - 'V' (Vrai) if the digit is correct and in the correct position.
        - 'P' (Passe) if the digit is correct but in the wrong position.
        - 'F' (Faux) if the digit is incorrect.

3. **Validate Guess**:
    - The function `is_valid_guess(guess)` checks if the player's guess is a valid 4-digit number with unique digits.

4. **Play Game**:
    - The function `play_game()` manages the game flow:
        - Prompts the player to enter their name.
        - Explains the rules of the game.
        - Allows the player up to 5 attempts to guess the secret number.
        - Provides feedback for each guess.
        - Congratulates the player if they guess the number correctly.
        - Reveals the secret number if the player fails to guess it within 5 attempts.
        - Asks the player if they want to play again.

## How to Run

To play the game, simply run the `mini-projet4.py` script in a Python environment. The game will prompt you for input and guide you through the process.

```bash
python mini-projet4.py
```

Enjoy the game!
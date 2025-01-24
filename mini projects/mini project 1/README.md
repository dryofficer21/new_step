# Mini Projet 1

This project is a simple Python calculator that supports various mathematical operations. The user can choose from a list of operations and perform calculations accordingly.

## Features

- **Addition**: Adds two numbers.
- **Soustraction**: Subtracts the second number from the first number.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides the first number by the second number (if the second number is not zero).
- **Puissance**: Raises the first number to the power of the second number.
- **Racine Carrée**: Calculates the square root of a number (if the number is non-negative).
- **Logarithme**: Calculates the natural logarithm of a number (if the number is positive).
- **Plusieurs Operations**: Evaluates a mathematical expression entered by the user.
- **Quitter**: Exits the calculator.

## Usage

1. Run the script `mini-projet1.py`.
2. Follow the on-screen instructions to choose an operation.
3. Enter the required numbers or expressions as prompted.
4. The result of the operation will be displayed.
5. You can choose to perform another operation or exit the calculator.

## Functions

- `addition(x, y)`: Returns the sum of `x` and `y`.
- `soustraction(x, y)`: Returns the difference of `x` and `y`.
- `multiplication(x, y)`: Returns the product of `x` and `y`.
- `division(x, y)`: Returns the quotient of `x` divided by `y` (if `y` is not zero).
- `puissance(x, y)`: Returns `x` raised to the power of `y`.
- `racine_carree(x)`: Returns the square root of `x` (if `x` is non-negative).
- `logarithme(x)`: Returns the natural logarithm of `x` (if `x` is positive).
- `get_expression_input(prompt)`: Prompts the user to enter a mathematical expression and evaluates it.
- `quitter()`: Exits the program.
- `get_number_input(prompt)`: Prompts the user to enter a number and returns it.
- `calcul()`: Main function that handles user input and performs the chosen operation.

## Example

```sh
python mini-projet1.py
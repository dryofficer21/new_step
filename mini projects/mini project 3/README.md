# Mini Project 3 - Restaurant Menu Management

This project consists of a simple restaurant menu management system implemented in Python. It allows users to view the menu, place orders, and manage the menu items (add, modify, delete). The menu data is stored in a JSON file.

## Files

### `menu.json`

This file contains the restaurant menu in JSON format. It includes categories such as "Entrées", "Plats principaux", "Desserts", and "Boissons".

### `menu_utils.py`

This file contains utility functions for loading and saving the menu from/to the JSON file.

- `sauvegarder_menu(menu, fichier)`: Saves the menu to the specified JSON file.
- `charger_menu(fichier)`: Loads the menu from the specified JSON file. If the file does not exist, it returns a default menu.

### `mini-projet3.py`

This file contains the main program logic for the restaurant menu management system.

- `afficher_menu(menu)`: Displays the menu.
- `passer_commande(menu)`: Allows the user to place an order by selecting items from the menu.
- `voir_addition(commande, total)`: Displays the order summary and total amount to be paid.
- `ajouter_plat(menu)`: Allows the administrator to add a new dish to the menu.
- `modifier_plat(menu)`: Allows the administrator to modify an existing dish in the menu.
- `supprimer_plat(menu)`: Allows the administrator to delete a dish from the menu.
- `verifier_entree(choix, options)`: Validates user input against a list of options.
- `menu_principal()`: The main function that runs the menu management system. It provides options to view the menu, place an order, see the bill, and manage the menu (admin only).

## Usage

1. Run the `mini-projet3.py` script to start the program.
2. Follow the on-screen instructions to navigate through the menu options.
3. Use the administrator password (`admin123`) to access the menu management functionalities.

```bash
python mini-projet3.py
```

## Requirements

- Python 3.x
- `menu.json` file in the same directory as the scripts

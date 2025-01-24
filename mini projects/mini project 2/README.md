# Mini-Project 2

## Description
This project is a simple task manager in Python. It allows managing a list of tasks with functionalities to add, display, mark as completed, delete, and save tasks.

## Features

1. **Afficher les tâches**
   - Displays the current list of tasks.
   - If the list is empty, a message indicating that the list is empty is displayed.

2. **Ajouter une tâche**
   - Allows adding a new task to the list.
   - The user is prompted to enter the description of the new task.

3. **Marquer une tâche comme terminée**
   - Allows marking an existing task as completed.
   - The user must enter the number of the task to mark as completed.
   - The task is updated with the addition of "[DONE]" at the end of the description.

4. **Supprimer une tâche**
   - Allows deleting a task from the list.
   - The user must enter the number of the task to delete.

5. **Sauvegarder et quitter**
   - Saves the list of tasks to a text file (`tasks.txt`).
   - Exits the program after saving.

## Usage

1. Run the Python script.
2. Follow the displayed instructions to interact with the task manager.
3. Choose from the menu options to manage your tasks.

## Task File

- Tasks are saved in a text file named `tasks.txt`.
- The file is automatically loaded at the start of the program to retrieve previously saved tasks.

## Example Execution

```
Bienvenue dans votre gestionnaire de tâches !
1. Afficher les tâches
2. Ajouter une tâche
3. Marquer une tâche comme terminée
4. Supprimer une tâche
5. Sauvegarder et quitter
Votre choix : 2
Entrez la nouvelle tâche : Acheter du lait
Tâche ajoutée avec succès.
Voulez-vous faire autre chose ? (oui/non) : oui
1. Afficher les tâches
2. Ajouter une tâche
3. Marquer une tâche comme terminée
4. Supprimer une tâche
5. Sauvegarder et quitter
Votre choix : 1
1. Acheter du lait
Voulez-vous faire autre chose ? (oui/non) : non
Au revoir!
```

## Author
This project was created by Ilyass FAKHTAOUI.
import os

FICHIER_TACHES = "taches.txt"

def afficher_taches(taches):
    """Affiche la liste des tâches."""
    if not taches:
        print("La liste des tâches est vide.")
    else:
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")

def ajouter_tache(taches):
    """Ajoute une nouvelle tâche à la liste."""
    tache = input("Entrez la nouvelle tâche : ")
    taches.append(tache)
    print("Tâche ajoutée avec succès.")

def marquer_tache_terminee(taches):
    """Marque une tâche comme terminée."""
    afficher_taches(taches)
    try:
        numero = int(input("Entrez le numéro de la tâche à marquer comme terminée : "))
        if 1 <= numero <= len(taches):
            taches[numero - 1] += " [FAIT]"
            print("Tâche marquée comme terminée.")
        else:
            print("Numéro de tâche invalide.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un numéro.")

def supprimer_tache(taches):
    """Supprime une tâche de la liste."""
    afficher_taches(taches)
    try:
        numero = int(input("Entrez le numéro de la tâche à supprimer : "))
        if 1 <= numero <= len(taches):
            taches.pop(numero - 1)
            print("Tâche supprimée avec succès.")
        else:
            print("Numéro de tâche invalide.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un numéro.")

def sauvegarder_taches(taches, fichier):
    """Sauvegarde les tâches dans un fichier."""
    with open(fichier, 'w') as f:
        for tache in taches:
            f.write(tache + '\n')
    print("Tâches sauvegardées.")

def charger_taches(fichier):
    """Charge les tâches à partir d'un fichier."""
    if os.path.exists(fichier):
        with open(fichier, 'r') as f:
            return [ligne.strip() for ligne in f]
    return []

def afficher_menu():
    """Affiche le menu des options."""
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Sauvegarder et quitter")

def menu():
    """Affiche le menu principal et gère les interactions utilisateur."""
    taches = charger_taches(FICHIER_TACHES)
    print("\nBienvenue dans votre gestionnaire de tâches !")
    while True:
        afficher_menu()
        choix = input("Votre choix : ")
        if choix == '1':
            afficher_taches(taches)
        elif choix == '2':
            ajouter_tache(taches)
        elif choix == '3':
            marquer_tache_terminee(taches)
        elif choix == '4':
            supprimer_tache(taches)
        elif choix == '5':
            sauvegarder_taches(taches, FICHIER_TACHES)
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
        
        continuer = input("Voulez-vous faire autre chose ? (oui/non) : ")
        if continuer.lower() != 'oui':
            print("Au revoir!")
            break

menu()
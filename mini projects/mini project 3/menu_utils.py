import json
import os

def sauvegarder_menu(menu, fichier):
    with open(fichier, 'w') as f:
        json.dump(menu, f, indent=4)
    print("Menu sauvegardé.")

def charger_menu(fichier):
    if os.path.exists(fichier):
        with open(fichier, 'r') as f:
            return json.load(f)
    return {
        "Entrées": {"Salade César": 5.00, "Soupe du jour": 4.50},
        "Plats principaux": {"Steak frites": 15.00, "Pâtes carbonara": 12.00},
        "Desserts": {"Tarte aux pommes": 6.00, "Mousse au chocolat": 5.50},
        "Boissons": {"Eau minérale": 2.00, "Café": 2.50}
    }

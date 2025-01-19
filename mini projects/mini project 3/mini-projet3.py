from menu_utils import charger_menu, sauvegarder_menu

def afficher_menu(menu):
    for categorie, plats in menu.items():
        print("\n" + categorie + ":")
        for plat in plats.keys():
            print("  - " + plat)

def passer_commande(menu):
    commande = []
    total = 0
    while True:
        afficher_menu(menu)
        choix = input("\nEntrez le nom du plat que vous souhaitez commander (ou tapez 'fin' pour terminer) : ")
        if choix == 'fin':
            break
        for plats in menu.values():
            if choix in plats:
                commande.append(choix)
                total += plats[choix]
                print(choix + " ajouté à la commande.")
                break
        else:
            print("Plat non trouvé dans le menu.")
    return commande, total

def voir_addition(commande, total):
    print("\nVotre commande :")
    for plat in commande:
        print("  - " + plat)
    print("Total à payer : " + "{:.2f}".format(total) + "€ \n")

def ajouter_plat(menu):
    categorie = input("Entrez la catégorie du plat : ")
    if categorie not in menu:
        menu[categorie] = {}
    plat = input("Entrez le nom du plat : ")
    prix = float(input("Entrez le prix du plat : "))
    menu[categorie][plat] = prix
    print(plat + " ajouté dans " + categorie + ".")

def modifier_plat(menu):
    categorie = input("Entrez la catégorie du plat à modifier : ")
    if categorie in menu:
        plat = input("Entrez le nom du plat à modifier : ")
        if plat in menu[categorie]:
            nouveau_nom = input("Entrez le nouveau nom du plat (ou appuyez sur Entrée pour ne pas changer) : ")
            nouveau_prix = input("Entrez le nouveau prix du plat (ou appuyez sur Entrée pour ne pas changer) : ")
            if nouveau_nom:
                menu[categorie][nouveau_nom] = menu[categorie].pop(plat)
                plat = nouveau_nom
            if nouveau_prix:
                menu[categorie][plat] = float(nouveau_prix)
            print(plat + " modifié avec succès. \n")
        else:
            print("Plat non trouvé. \n")
    else:
        print("Catégorie non trouvée. \n")

def supprimer_plat(menu):
    categorie = input("Entrez la catégorie du plat à supprimer : ")
    if categorie in menu:
        plat = input("Entrez le nom du plat à supprimer : ")
        if plat in menu[categorie]:
            del menu[categorie][plat]
            print(plat + " supprimé de " + categorie + ".")
        else:
            print("Plat non trouvé.")
    else:
        print("Catégorie non trouvée.")

def verifier_entree(choix, options):
    while choix not in options:
        print("Entrée invalide. Veuillez réessayer.\n")
        choix = input("Votre choix : ")
    return choix

def menu_principal():
    menu = charger_menu("menu.json")
    print("\nBienvenue dans le restaurant !")
    menu_modifie = False
    while True:
        print("\n1. Afficher le menu")
        print("2. Passer une commande")
        print("3. Voir l'addition")
        print("4. Gérer le menu (administrateur)")
        print("5. Quitter \n")

        choix = input("Votre choix : ")
        choix = verifier_entree(choix, ['1', '2', '3', '4', '5'])
        match choix:
            case '1':
                afficher_menu(menu)
            case '2':
                commande, total = passer_commande(menu)
            case '3':
                voir_addition(commande, total)
            case '4':
                admin_password = "admin123"  
                password = input("Entrez le mot de passe administrateur : ")
                if password == admin_password:
                    afficher_menu(menu)
                    print("\n1. Ajouter un plat")
                    print("2. Modifier un plat")
                    print("3. Supprimer un plat \n")
                    choix_admin = input("Votre choix : ")
                    choix_admin = verifier_entree(choix_admin, ['1', '2', '3'])
                    match choix_admin:
                        case '1':
                            ajouter_plat(menu)
                            menu_modifie = True
                        case '2':
                            modifier_plat(menu)
                            menu_modifie = True
                        case '3':
                            supprimer_plat(menu)
                            menu_modifie = True
                        case _:
                            print("Choix invalide.\n")
                else:
                    print("Mot de passe incorrect.\n")
            case '5':
                if menu_modifie:
                    sauvegarder_menu(menu, "menu.json")
                    print("Menu sauvegardé.")
                print("Au revoir! \n")
                break
            case _:
                print("Choix invalide. Veuillez réessayer. \n")

menu_principal()
import math
def addition(x,y):
    return x+y
def soustraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y != 0:
        return x/y
    else :
        print("impossible de diviser sur 0")
def puissance(x,y):
    return x**y
def racine_carree(x):
    if x < 0:
        return ValueError("Nombre négatif!")
    return math.sqrt(x)
def logarithme(x):
    if x <= 0:
        return ValueError("Nombre non positif!")
    return math.log(x)
def get_expression_input(prompt):
    while True:
        try:
            expression = input(prompt)
            result = eval(expression)
            return result
        except Exception :
            print("Veuillez entrer une expression valide.")
def quitter():
    exit()

def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

def calcul():
    print("Bienvenue dans la calculatrice Python ! Choisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance")
    print("6. Racine carrée")
    print("7. Logarithme")
    print("8. Plusieurs operations")
    print("9. Quitter")
    
    while True:
        try:
            oper = int(input("entrer votre choix (1-9) : "))
            if oper not in range(1, 10):
                raise ValueError
            break
        except ValueError:
            print("Choix invalide. Veuillez entrer votre choix (1-9) : ")

    match oper:
        case 1:
            a = get_number_input("entrer le premier nombre : ")
            b = get_number_input("entrer le deuxieme nombre : ")
            resultat = addition(a, b)
            print("resultat {} + {} = {}".format(a, b, resultat))
        case 2:
            a = get_number_input("entrer le premier nombre : ")
            b = get_number_input("entrer le deuxieme nombre : ")
            resultat = soustraction(a, b)
            print("resultat {} - {} = {}".format(a, b, resultat))
        case 3:
            a = get_number_input("entrer le premier nombre : ")
            b = get_number_input("entrer le deuxieme nombre : ")
            resultat = multiplication(a, b)
            print("resultat {} * {} = {}".format(a, b, resultat))
        case 4:
            a = get_number_input("entrer le premier nombre : ")
            b = get_number_input("entrer le deuxieme nombre : ")
            resultat = division(a, b)
            print("resultat {} / {} = {}".format(a, b, resultat))
        case 5:
            a = get_number_input("entrer le premier nombre : ")
            b = get_number_input("entrer le deuxieme nombre : ")
            resultat = puissance(a, b)
            print("resultat {} ^ {} = {}".format(a, b, resultat))
        case 6:
            a = get_number_input("entrer un nombre : ")
            resultat = racine_carree(a)
            print("resultat = ", resultat)
        case 7:
            a = get_number_input("entrer un nombre : ")
            resultat = logarithme(a)
            print("resultat = ", resultat)
        case 8:
            expression = get_expression_input("Entrez une expression mathématique (par exemple : 5 + 3 * 2) : ")
            print(f"Résultat de l'expression : {expression}")
        case _:
            quitter()
    choice = input("Voulez-vous effectuer une autre opération ? (oui/non) :")
    if choice == "oui" or choice == "OUI":
        calcul()
    else:
        breakpoint

calcul()
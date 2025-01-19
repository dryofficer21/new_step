import random

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def get_feedback(secret, guess):
    feedback = []
    for i in range(4):
        if guess[i] == secret[i]:
            feedback.append('V')
        elif guess[i] in secret:
            feedback.append('P')
        else:
            feedback.append('F')
    return feedback

def is_valid_guess(guess):
    return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4

def play_game():
    secret_number = generate_secret_number()
    attempts = 0
    max_attempts = 5

    name = input("Veuillez entrer ton nom : ")
    print("Bienvenue {}, je suis un programme intelligent".format(name))
    print('Je vais jouer avec toi le jeu "Vrai, Passe, Faux" !')
    print("J’ai choisi un nombre secret à 4 chiffres différents.")
    print("Vous avez 5 tentatives pour trouver mon nombre !")
    print("Est-ce vous êtes prêts :")

    while attempts < max_attempts:
        guess = input("Tentative {} : Entrez un nombre à 4 chiffres : ".format(attempts + 1))
        if not is_valid_guess(guess):
            print("Erreur : Veuillez entrer un nombre à 4 chiffres différents.")
            continue

        feedback = get_feedback(secret_number, guess)
        feedback_str = ', '.join(f"{guess[i]} {feedback[i]} ({'Vrai' if feedback[i] == 'V' else 'Passe' if feedback[i] == 'P' else 'Faux'})" for i in range(4))
        print("Résultat les chiffres : ", feedback_str)

        if feedback == ['V', 'V', 'V', 'V']:
            print("Félicitations ! Vous avez trouvé le nombre secret : {}".format(secret_number))
            break

        attempts += 1

    if attempts == max_attempts:
        print("Désolé, vous avez atteint le nombre maximum de tentatives. Le nombre secret était : {}".format(secret_number))

    replay = input("Voulez-vous rejouer ? (oui/non) : ").strip().lower()
    if replay == 'oui':
        play_game()

play_game()

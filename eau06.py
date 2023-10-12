import sys

args = sys.argv[1:]

# fonction pour mettre en majuscule une lettre sur deux
def make_upper():
    message = args[0]
    liste = []
    n = 2
    for letter in message:
        if letter == " ":
            liste.append(letter)
            continue
        elif n % 2 == 0:
            liste.append(letter.upper())
            n += 1
            continue
        elif n % 2 != 0:
            liste.append(letter.lower())
            n += 1
            continue
    print(liste)
    upp = "".join(liste)
    return upp


# vérification de l'entrée
if len(args) != 1 or args[0].isdigit():
    print("error")
    sys.exit()

# appel de la fonction
sentence = make_upper()

# affichage du résultat
print(sentence)

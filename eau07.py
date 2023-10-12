import sys

args = sys.argv[1:]


# fonction pour renvoyer une liste de mot
def split_list(arg):
    word = "".join(arg)
    liste = word.split()
    return upper_words(liste)


# fonction pour mettre en majuscule la première lettre de chaque mot
def upper_words(liste):
    list_upper = []
    for word in liste:
        list_upper.append(word.capitalize())
    upper_word = " ".join(list_upper)
    return upper_word


# vérification de l'entrée
if len(args) != 1 or args[0].isdigit():
    print("error")
    sys.exit()

# appel de la fonction
upper_word = split_list(args[0])

# affichage du résultat
print(upper_word)
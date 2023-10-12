import sys

args = sys.argv[1:]

# fonction pour afficher les nombres entre deux nombres
def number_btw(a, b):
    list_btw = []
    for n in range(a, b):
        if n == a:
            continue
        elif n != b:
            list_btw.append(str(n))
        else:
            continue

    nb_btw = " ".join(list_btw)
    return nb_btw

# vérification de l'entrée
if len(args) != 2:
    print("error")
    sys.exit()

# assignaton des variables
first_nb = args[0]
second_nb = args[1]

# vérification de l'entrée
if not first_nb.isdigit() or not second_nb.isdigit():
    print("error")
    sys.exit()

# appel de la fonction
nb = number_btw(int(first_nb), int(second_nb))

# affichage du résultat
print(nb)
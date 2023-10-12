from sys import argv, exit

args = argv[1:]


# fonction pour trouver la valeur de la différence absolue la plus petite
def absolute_minimal(liste):
    minimal_list = []

    for x in liste:
        for m in liste:
            if x != m:
                value = (int(x) - int(m))
                minimal_list.append(abs(value))
                continue
            continue
    min_value = min(minimal_list)
    return min_value


# vérification de l'entrée
for n in args:
    try:
        float(n)
    except:
        print("error")
        exit()
if len(args) < 3:
    print(args)
    print("error")
    exit()

# appel de la fonction
resultat = absolute_minimal(args)

# affichage du résultat
print(resultat)

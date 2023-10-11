import sys

args = sys.argv[1:]


def is_primary(nb):
    i = 2
    while i < nb:
        if nb % i == 0:
            print("nombre suivant...")
            return False
        i += 1
    return True


def next_primary(nb):
    n = nb + 1
    while not is_primary(n):
        n += 1

    return n


if len(args[0]) < 1 or not args[0].isdigit():
    print("erreur d'argument ")
    sys.exit()
elif int(args[0]) < 0:
    print("chiffre trop petit")
    sys.exit()


resultat = next_primary(int(args[0]))


print(resultat)

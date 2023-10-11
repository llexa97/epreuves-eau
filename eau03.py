import sys

# création des variable initial
args = sys.argv[1:]
fibo_list = []


# Fonction qui crée la liste fibonacci
def create_fibo_list(valeur):
    a = 0
    b = 1
    if len(fibo_list) < 2:
        fibo_list.append(a)
        fibo_list.append(b)
    for i in range(0, valeur - 1):
        a = fibo_list[-2]
        b = fibo_list[-1]

        fibo_list.append(a + b)
    return fibo_list[valeur]


# Gestion des erreur
if not args[0].isdigit():
    print(-1)
    sys.exit()
elif int(args[0]) <= 0:
    print(-1)
    sys.exit()


# Valeur chercher :
n = int(args[0])
resutat = create_fibo_list(n)

# Affichage du resultat
print(resutat)

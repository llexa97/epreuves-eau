# Création de la combinaison de chiffre
def combinaison():
    combinaisons = []
    for a in range(0, 10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                combinaison = f"{a}{b}{c}"
                combinaisons.append(combinaison)
    return combinaisons


# Création de la chaine de caractère
string = " , ".join(combinaison())

# affichage de la chaine de caractère
print(string)
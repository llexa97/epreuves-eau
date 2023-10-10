# Création de la premiere combinaison de chiffre
def combinaison():
    combinaisons = []
    a = 0 
    b = 0
    c = 0
    d = 1
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0,10):
                for d in range(1,10):
                    first_nmb = int(f"{a}{b}")
                    second_nmb = int(f"{c}{d}")
                    if first_nmb < second_nmb:
                        combinaison = f"{a}{b} {c}{d}"
                        combinaisons.append(combinaison)
                    else:
                        continue
    return combinaisons

# Création de la chaine de caractère
string = " , ".join(combinaison())

# affichage de la chaine de caractère
print(string)
from sys import argv, exit

args = argv[1:]


# fonction tri à bulle
def bubble_sort(array):
    permutation = True
    while permutation:
        permutation = False
        for i in range(0, (len(array) - 1)):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                permutation = True
    array = " ".join(array)
    return array


# verification si la liste contient des strings
def is_number(array):
    for i in array:
        try:
            int(i)
        except:
            return False
    return True


# veroification de l'entrée
if not is_number(args):
    print("error: strings are not accepted ")
    exit()

# appel de la fonction
sorted_list = bubble_sort(args)

# affichage du résultat
print(sorted_list)

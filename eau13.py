from sys import argv, exit

args = argv[1:]


def sort_selection(array):
    n = len(array)

    for i in range(0, n):
        mini = i
        for j in range(i + 1, n):
            if array[j] < array[mini]:
                mini = j
        if array[mini] != array[i]:
            array[i], array[mini] = array[mini], array[i]
            print(array)
    array = " ".join(array)

    return array


def is_number(array):
    for i in array:
        try:
            int(i)
        except ValueError:
            return False
    return True


if not is_number(args):
    print("error.")
    exit()

list_sorted = sort_selection(args)

print(list_sorted)


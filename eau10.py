import sys

args = sys.argv[1:]


def index_finder(liste, finder):
    if finder in liste:
        return liste.index(finder)
    return -1


if len(args) < 3:
    print("error")
    sys.exit()

finder = args[-1]
liste = args[:-1]

indexer = index_finder(liste, finder)

print(indexer)

import sys

args = sys.argv[1:]


def is_number(arg):
    nb = arg
    try:
        int(nb)
        return True
    except:
        return False


if len(args) != 1:
    print("error")
    sys.exit()

number = is_number(args[0])

print(number)

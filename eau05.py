import sys

args = sys.argv[1:]


def string_in_string() -> bool:
    arg_1 = args[0]
    arg_2 = args[1]
    if arg_2 in arg_1:
        return True
    return False


if len(args) != 2:
    print("error")
    sys.exit()
elif args[0].isdigit() or args[1].isdigit():
    print("error")
    sys.exit()


resultat = string_in_string()

print(resultat)

import sys 

# Get the arguments list
args = sys.argv[1:]

# Reverse the arguments list
def reserve_args(args):
    args.reverse()
    reverse_args = "\n".join(args)
    return reverse_args

# check if the arguments list is empty
if args == []:
    print("No arguments given")
    sys.exit()
    
# Print the reversed arguments list
print(reserve_args(args))
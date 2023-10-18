from sys import argv, exit

def argTest():
    args = argv[1:]
    
    data = []
    
    if len(args) < 2:
        print("error: not enough arguments")
        exit()
        return False
    
    for arg in args:
        argObj = {
            "argStr": arg,
            "argAscii": getAsciiValue(arg)
        }
        data.append(argObj)
        
    return data

def getAsciiValue(arg):
    return [ord(char) for char in arg]

def objAreSorted(obj1, obj2):
    shorter = min(len(obj1["argAscii"]), len(obj2["argAscii"]))
    
    for i in range(shorter):
        if obj1["argAscii"][i] < obj2["argAscii"][i]:
            return True
        return False
    
    return len(obj1["argAscii"]) < len(obj2["argAscii"])



def bubbleSort(array):
    permut = True
    
    while permut:
        permut = False
        print(array)
        for i in range(0, len(array) - 1):
            if not objAreSorted(array[i], array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                permut = True
    return array

def main():
    data = argTest()
    
    if data:
        sortedData = bubbleSort(data)
        result = [obj["argStr"] for obj in sortedData]
        print(" ".join(result))

main()

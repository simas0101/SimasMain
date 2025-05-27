import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1],"r") as file:
        length = 0
        for i in file:
            if i.lstrip().rstrip().startswith("#") == False and len(i.lstrip().rstrip()) > 0:
                length += 1
        print(length)
except FileNotFoundError:
    sys.exit("File does not exist")


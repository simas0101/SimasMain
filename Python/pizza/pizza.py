import sys
from tabulate import tabulate
import csv

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

try:
    table = []
    headers = []

    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        n = 0
        for line in reader:
            if n == 0:
                headers.append(line[0])
                headers.append(line[1])
                headers.append(line[2])
                n += 1
            else:
                table.append(line)

    print(tabulate(table, headers, tablefmt="grid"))


except FileNotFoundError:
    sys.exit("File does not exist")

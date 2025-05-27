import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")


try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        with open(sys.argv[2], "w", newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                name = row["name"]
                house = row["house"]
                last, first = name.rstrip().split(",")
                writer.writerow({"first": first.lstrip(), "last": last, "house": house})

except FileNotFoundError:
    sys.exit("File does not exist")
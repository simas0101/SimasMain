import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

designs = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    design = random.choice(designs)
    print(figlet.renderText(text))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in designs:
            text = input("Input: ")
            figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(text))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")



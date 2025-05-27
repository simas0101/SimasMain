import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"\bum\b", s, re.IGNORECASE)
    if um:
        counted = len(um)
    else:
        counted = 0
    return counted



if __name__ == "__main__":
    main()

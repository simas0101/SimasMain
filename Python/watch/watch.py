import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches =  re.search(r'<iframe[^>]*src=["\'](https?://(?:www\.)?youtube\.com/embed/([^"\']+))["\'][^>]*>', s)
    if matches:
        return f"https://youtu.be/{matches.group(2)}"





if __name__ == "__main__":
    main()
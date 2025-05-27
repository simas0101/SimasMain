import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")

def convert(s):

    pattern = "(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    matches = re.search(r"^" + pattern + r" to " + pattern + "$", s)
    if matches:
        from_when = check(matches.group(1), matches.group(2), matches.group(3))
        to_when = check(matches.group(4), matches.group(5), matches.group(6))
        return f"{from_when} to {to_when}"
    else:
        raise ValueError



def check(h, min, ampm):
    if h == "12":
        if ampm == "AM":
            hours = "00"
        else:
            hours = "12"
    else:
        if ampm == "AM":
            hours = f"{int(h):02}"
        else:
            hours = f"{int(h)+12}"

    if min == None:
        minutes = "00"
    else:
        minutes = f"{int(min):02}"
    return f"{hours}:{minutes}"

if __name__ == "__main__":
    main()

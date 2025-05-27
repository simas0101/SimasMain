def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if starts(s) and contains(s) and used(s) and allowed(s):
        return True
    else:
        return False

def starts(x):
    for i in x[0:2]:
        if i.isalpha():
            valid = True
        else:
            return False
    return valid


def contains(y):
    if 2 <= len(y) <= 6:
        return True
    else:
        return False

def used(z):
    digit = False
    for i in z:
        if i.isdigit():
            if not digit and i == '0':
                return False
            digit = True
        elif digit:
            return False
    return True


def allowed(q):
    for i in q:
        if i.isdigit() or i.isalpha():
            valid = True
        else:
            return False
    return valid

main()
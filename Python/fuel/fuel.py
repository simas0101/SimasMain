def main():
    z = get_fraction()
    print(z)

def get_fraction():
    while True:
        try:
            x,y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            z = round(x / y * 100)
            if 1 < z < 99:
                return str(z) + "%"
            elif z <= 1:
                return "E"
            elif z >= 99 and z <= 100:
                return "F"
        except (ValueError, ZeroDivisionError):
            pass



main()
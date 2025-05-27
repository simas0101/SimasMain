import inflect

def main():
    my_list = get_names()
    print("Adieu, adieu, to", my_list)

def get_names():
    p = inflect.engine()
    my_list = []
    while True:
        try:
            names = input("Name: ")
            my_list.append(names)
        except(EOFError, KeyError):
            print()
            break
        else:
            pass
    return p.join(my_list)

main()


def main():
    groceries_list = get_list()
    count(groceries_list)


def get_list():
    groceries_list = []
    while True:
        try:
            groceries = input().upper()
            groceries_list.append(groceries)
            groceries_list = sorted(groceries_list)
        except(EOFError, KeyError):
            break
        else:
            pass
    return groceries_list

def count(l):
    for i in l:
        if l.count(i) > 1:
            print(l.count(i), i)
            l.remove(i)
        else:
            print(l.count(i), i)




main()
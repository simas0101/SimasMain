s = input("camelCase: ")
mylist = []
for c in s:
    if c.isupper():
        mylist.append("_")
        mylist.append(c.lower())
    else:
        mylist.append(c)

snake_case = "".join(mylist)
print("snake_case:", snake_case)


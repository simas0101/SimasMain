x,y,z = input("Expression: ").split()
x = float(x)
z = float(z)
if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)
elif y == "/" and z != 0:
    print(x/z)
else:
    print("Error")
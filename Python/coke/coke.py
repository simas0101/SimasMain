amount = 0
amount_due = 50
while amount < 50:
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        amount = amount + coin
        amount_due = 50 - amount
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        elif amount_due == 0:
            print(f"Change Owed: 0")
        elif amount > 50:
            print(f"Change Owed: {amount - 50}")
    else:
        print(f"Amount Due: {amount_due}")
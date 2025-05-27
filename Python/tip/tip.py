def dollars_to_float(d):
    dol = d.replace("$","")
    return float(dol)

def percent_to_float(p):
    per = p.replace("%","")
    per = float(per)
    return per / 100


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()
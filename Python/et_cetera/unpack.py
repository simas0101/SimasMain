def total(galleons, sickles, knuts):
    return((galleons * 17 + sickles) * 29 + knuts)

coins1 = [100, 50, 25]
coins2 = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(*coins1), "Knuts")
print(total(**coins2), "Knuts")

def f(*args, **kwargs):
    print("Positional: ", args)
f(100, 50, 25)

def d(*args, **kwargs):
    print("Named: ", kwargs)
d(galleons=100, sickles=50, knuts=25)
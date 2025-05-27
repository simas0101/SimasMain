import requests
import sys

try:
    if len(sys.argv) != 1:
        n = float(sys.argv[1])
        if type(n) == float:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            o = response.json()
            price = o["bpi"]["USD"]["rate_float"]
            amount = price * n
            print(f"${amount:,.4f}")
        else:
            print("Command-line argument is not a number")
            sys.exit()
    else:
        print("Missing command-line argument")
        sys.exit(1)


except requests.RequestException:
    sys.exit()

def main():
    greet = input("Greeting: ").strip().lower()
    print(f"${value(greet)}")

def value(text):
    if text.startswith("hello"):
        return 0
    elif text.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
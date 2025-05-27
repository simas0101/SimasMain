import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        a,b = generate_integer(level)
        tries = 0
        while tries < 3:
            try:
                answer = a + b
                guess = int(input(f"{a} + {b} = "))
                if guess == answer:
                    score = score + 1
                    break
                elif guess != answer and tries == 2:
                    print(f"{a} + {b} = {answer}")
                    tries = tries + 1
                    break
                else:
                    print("EEE")
                    tries = tries + 1
            except ValueError:
                print("EEE")
                pass
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    elif level == 3:
        a = random.randint(100, 999)
        b = random.randint(100, 999)
    return a,b


if __name__ == "__main__":
    main()
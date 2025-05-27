import random
guesses = 0
while True:
    try:
        level = int(input("Level: "))
        number = random.randint(1, level)

        while True:
            guess = int(input("Guess: "))
            if guess < number:
                print("Too small!")
                guesses += 1
                pass
            elif guess > number:
                print("Too large!")
                guesses += 1
                pass
            elif guess == number:
                print("Just right!")
                guesses += 1
                break

    except ValueError:
        pass
    else:
        break
print("Guesses:", guesses)

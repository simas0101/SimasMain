def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")

def shorten(word):
    vowels = ["a", "o", "i", "u", "e", "A", "O", "I", "U", "E"]
    result = []
    for c in word:
        if c not in vowels:
            result.append(c)
    output = "".join(result)
    return output

if __name__ == "__main__":
    main()
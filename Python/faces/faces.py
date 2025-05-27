def convert(input_str):

    input_str = input_str.replace(':)', '🙂')

    input_str = input_str.replace(':(', '🙁')

    return input_str

def main():
    user_input = input("Enter text: ")
    converted_string = convert(user_input)
    print("Converted text:", converted_string)

main()

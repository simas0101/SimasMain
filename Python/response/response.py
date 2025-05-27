import validators
email = input("What's your email address? ").strip()

true = validators.email(email)

if true:
    print("Valid")
else:
    print("Invalid")
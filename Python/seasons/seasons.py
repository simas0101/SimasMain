from datetime import date
import inflect
import sys

class BirthDate:
    def __init__(self, date):
        self.date = date

def main():
    try:
        date_str = input("Date of Birth: ")
        birth_date = get_date(date_str)
    except ValueError:
            sys.exit("Invalid date")
    time_in_minutes = converted(birth_date)
    words = inflect.engine().number_to_words(time_in_minutes, andword="").capitalize()
    print(f"{words} minutes")

def get_date(date_str):
    try:
        year, month, day =  date_str.split('-')
    except ValueError:
        raise ValueError
    year = int(year)
    month = int(month)
    day = int(day)
    return BirthDate(date(year, month, day))

def converted(birth_date):
    today = date.today()
    time_delta = today - birth_date.date
    time_in_minutes = time_delta.days * 24 * 60
    return time_in_minutes

if __name__ == "__main__":
    main()

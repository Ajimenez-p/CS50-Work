"""
In a file called seasons.py, implement a program that prompts the user for their date of birth
in YYYY-MM-DD format and then prints how old they are in minutes, rounded to the nearest
integer, using English words instead of numerals, just like the song from Rent, without any and
 between words. Since a user might not know the time at which they were born, assume, for simplicity,
 that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time
 is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually
 midnight, on the same date. Use datetime.date.today to get today’s date, per
 docs.python.org/3/library/datetime.html#datetime.date.today.
"""

from datetime import date
import inflect
import sys

class Date:
    def __init__(self, date_string):
        try:
            year, month, day = map(int, date_string.split('-'))
            self.date = date(year, month, day)
        except:
            sys.exit()

    def __sub__(self, other):
        if isinstance(other, Date):
            delta = self.date - other.date
            return delta
        else:
            sys.exit()

    def __add__(self, other):
        if str(self) and str(other):
            added = self + other
            return added
        else:
            sys.exit()

    def minutes_since(self, other):
        delta = self - other
        minutes = delta.days * 24 * 60
        return minutes

def main():
    bday_str = input('Enter your birthdate: ')
    try:
        birth_date = Date(bday_str)
        today = Date(date.today().isoformat())
        minutes_old = today.minutes_since(birth_date)
        p = inflect.engine()
        minutes_in_words = p.number_to_words(minutes_old, andword='')
        print(minutes_in_words.capitalize() + ' minutes')
    except:
        sys.exit()

if __name__ == '__main__':
    main()

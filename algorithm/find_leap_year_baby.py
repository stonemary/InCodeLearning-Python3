# coding=utf-8
# By Ashwath from forums
# A leap year baby is a baby born on Feb 29, which occurs only on a leap year.
# Define a procedure is_leap_baby that takes 3 inputs: day, month and year
# and returns True if the date is a leap day (Feb 29 in a valid leap year)
# and False otherwise.
# A year that is a multiple of 4 is a leap year unless the year is
# divisible by 100 but not a multiple of 400 (so, 1900 is not a leap
# year but 2000 and 2004 are).
# We also have a wiki link regarding the algorithm to calculate leap years
# https://en.wikipedia.org/wiki/Leap_year


def is_leap_baby(day, month, year):  # define a function which use 3 inputs
    if year == 1900:
        return False
    if year % 100 == 0 & year % 400 != 0:
        return False

    elif year % 4 == 0:
        if day == 29 and month == 2:
            return True

    else:
        return False


# The function 'output' prints one of two statements based on whether
# the is_leap_baby function returned True or False.


def output(status, name):
    if status:
        print("%s is one of an extremely rare species."
              "He is a leap year baby!"
              % name)
    else:
        print("There's nothing special about %s's birthday."
              "He is not a leap year baby!"
              % name)


# Test Cases

print(output(is_leap_baby(29, 2, 1996), 'Calvin'))
# >>>Calvin is one of an extremely rare species.
# He is a leap year baby!
print(""" """)
print(output(is_leap_baby(19, 6, 1978), 'Garfield'))
# >>>There's nothing special about Garfield's birthday.
# He is not a leap year baby!
print(""" """)
print(output(is_leap_baby(29, 2, 2000), 'Hobbes'))
# >>>Hobbes is one of an extremely rare species.
#  He is a leap year baby!
print(""" """)
print(output(is_leap_baby(29, 2, 1900), 'Charlie Brown'))
# >>>There's nothing special about Charlie Brown's birthday.
# He is not a leap year baby!
print(""" """)
print(output(is_leap_baby(28, 2, 1976), 'Odie'))
# He is  not a leap year baby!

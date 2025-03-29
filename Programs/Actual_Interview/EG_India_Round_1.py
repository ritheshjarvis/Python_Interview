"""
Write a program to determine the day number of the year (1 to 365 for a non-leap year and 1 to 366 for a leap year)
without using built-in date functions like DayOfYear.

Input: "12-04-2021"

Output: 102

Phase 1:
Splitting input text into date, month and year format (integer)
first assuming every month has 30 days

Logic:
output = date + month * 30

Phase 2:
defining Dictinary for month number and day count

{1: 31, 2: 28, 3:}
month_list = [31, 28, 31, 30 ....]
month_list[1] = 29 --> if this is a leap year
even / odd -> approach

Leap year Logic:
if year // 4 == 0 --> then its a leap year
then for Feb month add + 1 (29 days) - > 366

Phase 3:

"""

input = "12-04-2021"
output = 0
day, month, year = input.split('-')
day, month, year = int(day), int(month), int(year)
print(day, month, year)

month_list = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]

if year % 4 == 0:
    print("leap year")
    month_list[1] = 29

for _month, _month_days in enumerate(month_list):
    if _month < month - 1:
        print(_month, _month_days)
        output = output + _month_days

output = output + day
print(output)

""" Solution 2 - Chartgpt ----------------------- 

To determine the day number of the year from a given date without using built-in date functions, we need to:

Extract the day, month, and year from the input string.

Check if the year is a leap year (to handle February correctly).

Use a lookup table for the number of days in each month and sum up the days from previous months.

Add the day of the given month to get the final day number.

"""


def is_leap_year(year):
    """Returns True if the given year is a leap year, otherwise False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def day_of_year(date_str):
    """Calculates the day number of the year without using built-in date functions."""

    # Parse input date (Format: "DD-MM-YYYY")
    day, month, year = map(int, date_str.split('-'))

    # Days in each month (Non-leap year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Update February for leap year
    if is_leap_year(year):
        month_days[1] = 29

    # Sum the days of the previous months + current day
    day_number = sum(month_days[:month - 1]) + day
    return day_number


# Example Usage
date_input = "12-04-2021"  # April 12, 2021
print(day_of_year(date_input))  # Output: 102

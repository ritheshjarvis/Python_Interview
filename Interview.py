"""
Write a program to determine the day number of the year (1 to 365 for a non-leap year and 1 to 366 for a leap year)
without using built-in date functions like DayOfYear.

Input: "12-04-2021"
Input: "01-01-2021"

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


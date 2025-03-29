year = 2021
#
if year % 4 == 0:
    print("leap year")

print(year / 4) # Whole Number # 505.25
print(year % 4) # Reminder # 505
print(year // 4) # Only Whole number without fraction # 505

fraction_part = (year / 4) % 1  # Get only the fractional part # 0.25
fraction_output = int(fraction_part * 100) # 25

print(fraction_output)


# ------------------ Leap Year -------------------
"""
How to Determine if a Year is a Leap Year?
A leap year occurs:
✅ If a year is divisible by 4 → It is a leap year except
✅ If a year is divisible by 100 → It is NOT a leap year unless
✅ If a year is divisible by 400 → It IS a leap year
"""

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Example Usage
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a Leap Year!")
else:
    print(f"{year} is NOT a Leap Year.")

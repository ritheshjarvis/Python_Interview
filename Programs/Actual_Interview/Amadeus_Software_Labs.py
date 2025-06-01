# Generate prime series of first 5 numbers

"""
 - A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself.
 - 1 is not a prime number:
 - The number 1 has only one factor (itself), so it does not meet the definition of a prime number.
 Ex: [2, 3, 5, 7, 11, 13, 17]
"""

def prime_check(number):
    if number <= 1:
        return False
    else:
        for item_ in range(2, number):
            if number % item_ == 0:
                return False
    return True

prime_series = []

num = 2
while len(prime_series) < 5:
    if prime_check(num):
        prime_series.append(num)
    num += 1

print("First 5 prime numbers:", prime_series)

# ------------ JSON ----- Assertion --------

json_string = '''{
  "name": "Rithesh",
  "age": 30,
  "isMarried": true,
  "children": ["Aryan", "Diya"],
  "address": {
    "city": "Mangalore",
    "state": "Karnataka",
    "pinCode": 575001
  }
}'''

import json

dict_value = json.loads(json_string)
print(dict_value)

# with open('test.json', 'r') as file:
#     dict_value = json.load(file)
#
# print(dict_value)

assert dict_value['address'][1] == "Mangalore1", "error happened"
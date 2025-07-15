# Generate prime series of first 5 numbers

# Trick - while(len(prime_series) < target):    

"""
 - A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself.
 - 1 is not a prime number:
 - The number 1 has only one factor (itself), so it does not meet the definition of a prime number.
 Ex: [2, 3, 5, 7, 11, 13, 17]
"""

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    else:
        for item in range(2, num):
            if num % item == 0:
                return False
    return True
    
target: int = 9
counter: int = 2
prime_series: list[int] = []

while(len(prime_series) < target):
    if is_prime(counter):
        prime_series.append(counter)
    counter += 1
    
print(prime_series)

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
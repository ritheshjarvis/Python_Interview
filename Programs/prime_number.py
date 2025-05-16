"""
 - A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself.
 - 1 is not a prime number:
 - The number 1 has only one factor (itself), so it does not meet the definition of a prime number.
 Ex: [2, 3, 5, 7, 11, 13, 17]
"""

def validate_prime(number: int) -> bool:
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for item in range(2, number):
            if number % item == 0:
                return False
        return True

print(validate_prime(9))

def return_prime_numbers(limit: int) -> list[int]:
    prime_number_list: list[int] = []

    for item in range(2, limit+1):
        if validate_prime(item):
            prime_number_list.append(item)
    return prime_number_list

print(return_prime_numbers(19))

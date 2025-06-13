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

if __name__ == "__main__":
    series_length = 5
    value = 0
    prime_series = []

    while len(prime_series) < series_length:
        if validate_prime(value):
            prime_series.append(value)
        value += 1

    print(f'Prime series: {prime_series}')

print(return_prime_numbers(19))

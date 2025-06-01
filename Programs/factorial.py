"""
Factorial of number of without recursion:
The Factorial of a whole number 'n' is defined as the product of that number with every whole number
less than or equal to 'n' till 1. For example, the factorial of 4 is 4 × 3 × 2 × 1, which is equal to 24.
"""

number = 4
output = 1

for item in range(1, number + 1):
    output = output * item

print(output)

# --------------------------- using reduce ---------------------------

from functools import reduce

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))

# Example usage
num = 5
print(f"Factorial of {num} is {factorial(num)}")

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0  # First Fibonacci number is 0
    elif n == 2:
        return 1  # Second Fibonacci number is 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example: Print first 10 Fibonacci numbers
num_terms = 10
print("Fibonacci Series:")
for i in range(1, num_terms + 1):
    print(fibonacci(i), end=" ")

# Fibonacci series without Recursion

def fibonacci_series(n):
    series = [0, 1]
    if n == 1:
        return series[0]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

n = 3
fib_series = fibonacci_series(n)
print(f"The first {n} numbers in the Fibonacci series are: {fib_series}")
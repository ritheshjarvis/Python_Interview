# Fibonacci series without Recursion 2

input_length = 5
fibonacci_series = [0, 1]

if input_length < 1:
    raise ValueError("Input Length should be greater than o")
elif input_length == 1:
    print(fibonacci_series[0])
elif input_length == 2:
    print(fibonacci_series)
else:
    for item in range(2, input_length):
        fibonacci_series.append(fibonacci_series[item - 1] + fibonacci_series[item - 2])

print(fibonacci_series)
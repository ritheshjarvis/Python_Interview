# Fibonacci series
# The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610

def fibbonacci_series(limit: int) -> list[int]:
    sequence = [0, 1]

    if limit <= 0:
        return []
    elif limit == 1:
        return [sequence[0]]
    elif limit == 2:
        return sequence
    else:
        for item in range(0, limit - 2):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence


if __name__ == "__main__":
    series = 5
    # print(fibbonacci_series(series))
#------------------------------------------------------------------
# Fibonacci Series without Recursion

def fibonacci_series(n):
    series = [0, 1]
    if n == 1:
        return series[0]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

def fibonacci_2(_count):
    _output = [0,1]
    if _count <= 1:
        return _output[0]
    elif _count == 2:
        return _output
    else:
        for _index in range(2, _count):
            _output.append(_output[-1] + _output[-2])
        return ''.join(_output)

if __name__ == '__main__':
    n = 5
    fib_series = fibonacci_series(n)
    print(f"The first {n} numbers in the Fibonacci series are: {fib_series}")


# ---------------------------------------------------------

# Fibonacci series

def fibonacci_series(target:int) -> list[int] | bool:
    fib_series = [0, 1]
    
    if target < 1:
        return False
    elif target == 1:
        return list(fib_series[0]);
    elif target == 2:
        return fib_series
    else:
        for item in range(2, target):
            fib_series.append(fib_series[item-1] + fib_series[item-2])
    return fib_series
    
target = 10
series = fibonacci_series(target)
if series:
    print(series)
else:
    print("Enter Positive Natural Number")
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
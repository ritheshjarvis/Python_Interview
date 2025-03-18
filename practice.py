

def factorial(_count):
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
    count = 5
    # output = factorial(count)
    # print(output)

    out = [1,2,3]
    print(str(out))
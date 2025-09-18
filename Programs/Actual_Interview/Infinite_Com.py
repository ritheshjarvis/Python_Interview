# First Program: Find is there any duplicate in a given list and return True of False

def validate_duplicate(input_: list) -> bool:
    original = []
    duplicate = []
    for item in input_:
        if item in original:
            return False
        else:
            original.append(item)
    return True

input_list = [1,3,4,5,6, 3]
print(validate_duplicate(input_list))

def validate_duplicate(input_ : list) -> bool:
    for item in input_:
        if input_.count(item) > 1:
            return False
    return True

def duplicate_check_2(input_):
    dict = {}
    
    for item in input_:
        if item not in dict.keys():
            dict[item] = None
        else:
            return True
    return False

input_list = [1,2,3,4]
print(validate_duplicate(input_list))

# Second Program: lamda function to get the square of number
output = list(map(lambda x:x*x, [1, 2, 5]))
print(output)
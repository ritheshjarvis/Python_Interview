# Reversing a string in Python with recursion

def reverse_function(input_string):
    if len(input_string) <= 1:
        return input_string
    return reverse_function(input_string[1:]) + input_string[:1]

def reverse_recursive(input_: str) -> str:
    if len(input_) <= 1:
        return input_
    else:
        return input_[len(input_) - 1] + reverse_recursive(input_[:len(input_) - 1])


input_str = "abcdefg"
output = reverse_function(input_str)
print(output)
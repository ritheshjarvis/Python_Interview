# Reversing a string in Python with recursion

def reverse_function(input_string):
    if len(input_string) <= 1:
        return input_string
    return reverse_function(input_string[1:]) + input_string[:1]


input_str = "abcdefg"
output = reverse_function(input_str)
print(output)
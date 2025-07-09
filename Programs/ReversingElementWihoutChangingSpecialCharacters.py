# Reversing a string without changing the special characters
# Two pointer technique

input_str = "ritheshb1@gmail.com"

input_list = list(input_str)

start = 0
end = len(input_list) - 1

while start < end:
    if not input_list[start].isalnum():
        start = start + 1
    elif not input_list[end].isalnum():
        end = end - 1
    else:
        input_list[start], input_list[end] = input_list[end], input_list[start]
        start = start + 1
        end = end - 1

print(''.join(input_list))


# Write a program to reverse a string without changing the special characters
# input = 'rithesh@gmail.com'

def reverse_string(input_str: str) -> str:
    print(input_str)
    input_list = list(input_str)
    start, end = 0, len(input_list) - 1
    while(start < end):
        if not input_list[start].isalnum():
            start += 1
        elif not input_list[end].isalnum():
            end -= 1
        else:
            input_list[start], input_list[end] = input_list[end], input_list[start]
            start += 1
            end -= 1
    return ''.join(input_list)
    
input = 'rithesh@gmail.com'
print(reverse_string(input))


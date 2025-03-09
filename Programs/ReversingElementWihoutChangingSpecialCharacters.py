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


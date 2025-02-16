# Reverse a String
input_str = "abcedefg"
output = []
output_str = ""

# Method 1 - Negative slice indexing
print(input_str[::-1])
# -----------------------------------
# Method 2 - using logic - prepending each character
for item in input_str:
    output_str = item + output_str

print(output_str)
# -----------------------------------
# Method 3 - Two Pointer technique with list
input_list = list(input_str)
start = 0
end = len(input_str) - 1

while start < end:
    input_list[start], input_list[end] = input_list[end], input_list[start]
    start = start + 1
    end = end - 1

print("".join(input_list))
# -----------------------------------
# Method 4 - using reversed() function
print(''.join(reversed(input_str)))
# -----------------------------------
# Method 5 - Negative step in range()
for i in range(len(input_str) - 1, -1, -1):
    output.append(input_str[i])
# -----------------------------------
# Method 6 - By Logic + range function
for item in range(len(input_str)):
    output.append(input_str[len(input_str) - 1 - item])
# -----------------------------------
# Method 7 - reversed function
for item in reversed(range(len(input_str))):
    output.append(input_str[item])

print(''.join(output))

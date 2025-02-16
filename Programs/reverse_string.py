# Reverse a String

# Method 1 - Negative slice indexing
input_str = "abcedefg"
print(input_str[::-1])

output = []

# Method 2 - Negative step in range()
for i in range(len(input_str) - 1, -1, -1):
    output.append(input_str[i])

# Method 3 - By Logic
for item in range(len(input_str)):
    output.append(input_str[len(input_str) - 1 - item])

# Method 3 - reversed function
for item in reversed(range(len(input_str))):
    output.append(input_str[item])

print(''.join(output))

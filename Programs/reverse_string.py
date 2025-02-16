# Reverse a String

# Method 1 - Negative slice indexing
input_str = "abcedefg"
print(input_str[::-1])

output = []

# Method 2 - using reversed() function
print(''.join(reversed(input_str)))

# Method 3 - Negative step in range()
for i in range(len(input_str) - 1, -1, -1):
    output.append(input_str[i])

# Method 4 - By Logic
for item in range(len(input_str)):
    output.append(input_str[len(input_str) - 1 - item])

# Method 5 - reversed function
for item in reversed(range(len(input_str))):
    output.append(input_str[item])

print(''.join(output))

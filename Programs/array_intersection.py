# Find the intersection of two arrays.

arr1 = [3, 5, 9, 0, 3, 1]
arr2 = [2, 4, 8, 0, 5, 3]
output = []

# Method 1 - Logic
for item in arr1:
    if item in arr2:
        output.append(item)

print(output)

# Method 2 - Set Intersection use
# First convert to Sets

output = list(set(arr1).intersection((set(arr2))))
print(output)
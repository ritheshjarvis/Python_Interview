# Find the duplicate element in a given list
input_list = [1,4,6,4,3,3]
original = []
duplicate = []

for item in input_list:
    if item in original:
        duplicate.append(item)
    else:
        original.append(item)

print(duplicate)
# Find the duplicate element in a given list
input_list = [1,4,6,4,3,3]
duplicate = []

for item in input_list:
    if input_list.count(item) > 1:
        duplicate.append(item)

print(duplicate)


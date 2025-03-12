# Find the duplicate element in a given list
input_list = [1,4,6,4,3,3]
duplicate = set()

for item in input_list:
    if input_list.count(item) > 1:
        duplicate.add(item)

print(list(duplicate))


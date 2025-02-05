# Find the duplicate element in a given list
input_list = [1,4,6,4,3,3]
freq = {}
duplicate = []

for item in input_list:
    if item in freq.keys():
        duplicate.append(item)
    else:
        freq[item] = None

print(duplicate)
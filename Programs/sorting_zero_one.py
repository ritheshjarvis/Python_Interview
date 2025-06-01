def sort_zeros_ones(input_list):
    zeros = input_list.count(0)
    ones = input_list.count(1)
    return [0] * zeros + [1] * ones

# Example usage
input_list = [1, 0, 1, 0, 1]
# output_list = sort_zeros_ones(input_list)
# print(output_list)  # Output: [0, 0, 0, 1, 1, 1]

# print([3] * 4)

out = []

for item in input_list:
    if item:
        out.append(item)
    else:
        out.insert(0, item)

print(out)


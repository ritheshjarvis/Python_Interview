# Main trick -> At inner loop -> range starts from outer+1

# From the given array -> Find a Pair of elements whose value is 6

input = [2, 6, 3, 3, 4]
target = 6
output = []
# output = [[2, 4], [3, 3]]

for outer in range(len(input)):
    print("Outer: ----- " + str(outer))
    for inner in range(outer + 1, len(input)):
        print("Inner: " + str(inner))
        print(outer, inner)
        if input[outer] + input[inner] == target:
            output.append([input[outer], input[inner]])

print(output)


## Find the frequency of each character in a given array

input = 'book'
out = {}

for item in input:
    if item not in out.keys():
        out[item] = 1
    else:
        out[item] += 1

print(out)

# Find pairs with sum equal to target
def find_pairs_with_sum(arr: list[int], target: int) -> list[list[int]]:
    output: list[list[int]] = []
    for outer in range(len(arr)):
        for inner in range(outer + 1, len(arr)):
            if arr[outer] + arr[inner] == target:
                output.append([arr[outer], arr[inner]])
    return output

# Find frequency of each character in a string
def char_frequency(s: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for item in s:
        if item not in out:
            out[item] = 1
        else:
            out[item] += 1
    return out

input_list: list[int] = [2, 6, 3, 3, 4]
target: int = 6
print(find_pairs_with_sum(input_list, target))

input_str: str = 'book'
print(char_frequency(input_str))
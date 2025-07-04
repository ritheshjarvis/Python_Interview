input = [3, 1, 2, 4, 5]

# Find a pair of numbers in the list that sum to a given value
# i need to return all the pairs that sum to the target value
def find_pair_with_sum(arr, target_sum):
    pairs = []
    for outer in range(len(arr)):
        for inner in range(outer + 1, len(arr)):
            if arr[outer] + arr[inner] == target_sum:
                pairs.append((arr[outer], arr[inner]))
    return pairs

# Example usage
target_sum = 5
result = find_pair_with_sum(input, target_sum)
if result:
    print(f"Pair found: {result}")
else:
    print("No pair found that sums to the target value.")
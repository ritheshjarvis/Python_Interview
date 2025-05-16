def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Optimization: Track if a swap happens
        for j in range(n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:  # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps in a pass, the array is already sorted
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)

# Correct method --- Look here ---

arr = [3, 10, 5, 2, 8, 1]

for _i in range(0, len(arr)):
    for _j in range(0, len(arr) - _i - 1):
        print(_j)
        if arr[_j] > arr[_j + 1]:
            arr[_j], arr[_j + 1] = arr[_j + 1], arr[_j]
    print(arr)

print(arr)

# Interview

input_list = [1, 5, 3, 8, 9]

for outer in range(len(input_list)):
    print("-------outer---" + str(outer))
    for inner in range(len(input_list) - 1 - outer):
        print(">>inner" + str(inner))
        if input_list[inner] > input_list[inner+1]:
            input_list[inner], input_list[inner+1] = input_list[inner+1], input_list[inner]


print(input_list)
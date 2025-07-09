# Binary Search - Sorted Array
# Two pointer technique - Devide and Conquer Method
# Find mid element
# if Mid element == target element -> return index
# if target element < target element -> end = mid

def binary_search(arr: list[int], target: int) -> int:
    start, end = 0, len(arr) - 1
    out_index = -1
    
    while start < end:
        # mid = int((end-start/2) - 1)
        mid = start + ((end - start) // 2)
        if arr[mid] == target:
            out_index = mid
            return out_index
        elif arr[mid] < target:
            end = mid
        elif arr[mid] > target:
            start = mid
    return out_index
    
    
input = [1, 4, 8, 9, 12, 13, 15]
target = 4
print(binary_search(input, target))

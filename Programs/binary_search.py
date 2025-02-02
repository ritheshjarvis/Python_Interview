# Binary Search

'''
Binary search is an efficient searching algorithm used to find an element in a sorted array. 
It follows the divide and conquer approach, repeatedly dividing the search space in half until
the element is found or the search space is empty.

Algorithm Steps:
Find the middle element of the array.
If the middle element is the target value, return its index.
If the target is smaller than the middle element, repeat the search on the left half.
If the target is greater than the middle element, repeat the search on the right half.
Continue this process until the element is found or the search space is empty.
'''

input_list = [3, 6, 8, 9, 10]
search = 2
out_index = -1
start = 0
end = len(input_list) - 1

while(start <= end):
    mid = start + ((end-start)//2)

    if input_list[mid] == search:
        out_index = mid
        break
    elif search < input_list[mid]:
        end = mid - 1
    else:
        start = mid + 1
        
print(f'Element found at : {out_index}' if out_index != -1 else "Element Not found")
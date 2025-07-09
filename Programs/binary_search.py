# Binary Search

'''
Binary search is an efficient searching algorithm used to find an element in a sorted array. 
It follows the divide and conquer approach and two pointer technique, repeatedly dividing the search space in half until
the element is found or the search space is empty.

Algorithm Steps:
Find the middle element of the array.
If the middle element is the target value, return its index.
If the target is smaller than the middle element, repeat the search on the left half.
If the target is greater than the middle element, repeat the search on the right half.
Continue this process until the element is found or the search space is empty.

Time Complexity:
    Best case: 
        O(1) (if the middle element is the target)
    Average case: 
        O(logn) (since the search space is divided in half each time)
    Worst case: 
        O(logn)
'''

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
search = 4
out_index = -1
start = 0
end = len(input_list) - 1

while(start <= end):
    mid = start + ((end-start)//2)
    print(f'Start: {start}, End: {end}, Mid: {mid}, Value at Mid: {input_list[mid]}')

    if input_list[mid] == search:
        out_index = mid
        break
    elif search < input_list[mid]:
        end = mid - 1
    else:
        start = mid + 1
        
print(f'Element found at : {out_index}' if out_index != -1 else "Element Not found")
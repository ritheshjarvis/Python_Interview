# Linear Search
'''
Concept: Traverses each element of the array one by one to find the target.
Time Complexity:
    Best case: 
        𝑂(1) - (if the element is at the start).
    Worst case: 
        𝑂(𝑛) - (if the element is at the end or not present).
Usage: Works on both sorted and unsorted arrays.
'''
def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
    return -1
    
arr = [4, 8, 2, 0, 6]
target = 2
out_index = linear_search(arr, target)
if out_index == -1:
    print("Target Not found")
else:
    print(f'Target - {target} found at {out_index}')
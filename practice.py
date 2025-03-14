# Binary Search

input_array = [1, 2, 3, 6, 9]
search = 3
start = 0
end = len(input_array)

out = 0

while end > start:
    mid = start + ((end-start)//2)
    if input_array[mid] == search:
       out = mid
       break
    elif input_array[mid] < search:
        start = mid + 1
    else:
        end = mid - 1

print(out)

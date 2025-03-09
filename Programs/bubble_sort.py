arr = [5, 3, 8, 6, 7, 2]
i = 0

while i < len(arr) - 1:
    if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
    i = i + 1

print(arr)
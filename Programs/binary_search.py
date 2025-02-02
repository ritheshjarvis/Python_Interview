input_list = [3, 6, 8, 9, 10]
search = 2
index = -1
start = 0
end = len(input_list) - 1

while(start <= end):
    mid = start + ((end-start)//2)

    if input_list[mid] == search:
        index = mid
        break
    elif search < input_list[mid]:
        end = mid - 1
    else:
        start = mid + 1
        
print(f'Element found at : {index}' if index != -1 else "Element Not found")
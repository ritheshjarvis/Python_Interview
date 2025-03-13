input_list = [[1,2,3], [4,5,6], [7, 8, 9]]
diagonal = []
antidiagonal = []

for key, _lst in enumerate(input_list):
    antidiagonal.append(_lst[len(_lst) - 1 - key])
    diagonal.append(_lst[key])

print(diagonal)
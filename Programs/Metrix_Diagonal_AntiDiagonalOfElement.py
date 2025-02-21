# Print the Diagonal of element

def diagonal(*args):
    diagonal_out = []
    for item in range(0, len(args)):
        diagonal_out.append(args[item][item])
    return diagonal_out

def anti_diagonal(*args):
    anti_diagonal_out = []
    for item in range(0, len(args)):
        anti_diagonal_out.append(args[item][(len(args) - 1) - item])
    return anti_diagonal_out


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = [7, 8, 9]
diagonal_out = diagonal(arr1, arr2, arr3)
print(diagonal_out)

anti_diagonal_out = anti_diagonal(arr1, arr2, arr3)
print(anti_diagonal_out)


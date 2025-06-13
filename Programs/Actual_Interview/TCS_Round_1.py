# Main trick -> In inner loop -> range starts from outer+1

# From the given array -> Find a Pair of elements whose value is 6

input = [2, 6, 3, 3, 4]
target = 6
output = []
# output = [[2, 4], [3, 3]]

for outer in range(len(input)):
    print("Outer: ----- " + str(outer))
    for inner in range(outer + 1, len(input)):
        print("Inner: " + str(inner))
        print(outer, inner)
        if input[outer] + input[inner] == target:
            output.append([input[outer], input[inner]])

print(output)


## Find the frequency of each character in a given array

input = 'book'
out = {}

for item in input:
    if item not in out.keys():
        out[item] = 1
    else:
        out[item] += 1

print(out)
# Main trick -> At inner loop -> range starts from outer+1

# Program -> Two find the pair whose difference is least

input_list = [10, 1, 11, 38, 67]
# expected output = [10, 11]
diff = max(input_list)
# diff = abs(input_list[1] - input_list[0])  # Initialize with the first pair's difference
output = []

for outer in range(len(input_list)):
    # print(outer)
    for inner in range(outer+1, len(input_list)):
        # print("---------" + str(inner))
        print(abs(input_list[inner] - input_list[outer]))
        if abs(input_list[inner] - input_list[outer]) < diff:
            diff = abs(input_list[inner] - input_list[outer])
            output = [input_list[inner], input_list[outer]]
            print("OUT----------", output)

print(output)
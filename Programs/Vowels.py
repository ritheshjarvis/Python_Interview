# Vowels count in a given string

input_str = "aabddefu"
output = {}

for item in input_str:
    if item.lower() in "aeiou":
        if item in output.keys():
            output[item] = output[item] + 1
        else:
            output[item] = 1

print(output)
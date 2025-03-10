input_str = "abcabcabcef"

output = {}

for _elem in input_str:
    if _elem in output.keys():
        output[_elem] = output[_elem] + 1
    else:
        output[_elem] = 1

print(output)

for index, (key, val) in enumerate(output.items()):
   print(index, key, val)
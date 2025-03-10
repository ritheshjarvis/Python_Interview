output: dict[int:str] = {1: 'one', 2: 'two', 3: 'three'}

# keys - dict.keys()
for key in output.keys():
    print(key)

# values - dict.values()
for val in output.values():
    print(val)

# items - dict.values()
for key, value in output.items():
    print(key, value)

# Enumerate function - gives index as well
for index, (key, val) in enumerate(output.items()):
   print(index, key, val)
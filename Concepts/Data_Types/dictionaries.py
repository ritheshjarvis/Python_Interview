# output: dict[int:str] = {1: 'one', 2: 'two', 3: 'three'}

# # keys - dict.keys()
# for key in output.keys():
#     print(key)
#
# # values - dict.values()
# for val in output.values():
#     print(val)
#
# # items - dict.values()
# for key, value in output.items():
#     print(key, value)
#
# # Enumerate function - gives index as well
# for index, (key, val) in enumerate(output.items()):
#    print(index, key, val)

# -------------------------------------------------
output: dict[int:str] = \
    {1: 'one', 2: 'two', 3: 'three'}

# To retrieve item value
print(output.get(1))  # one

# To add / update item vaule
output[2] = "TWO!"
print(output.get(2)) #TWO!
output[5] = "FIVE"
print(output.get(5))
print(output)
_input = [3, 6, 8, 6]
duplicate = set()

for _item in _input:
    if _input.count(_item) > 1:
        duplicate.add(_item)

print(list(duplicate))

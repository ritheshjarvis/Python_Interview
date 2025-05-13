# if all the itmes are covered in the loop, then only it will go to else block
list_ = [1, 2, 3, 4, 8]

for item in list_:
    if item == 3:
        print(item)
        break
else:
    print("All loop over")



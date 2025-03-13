class Parent:
    def __init__(self):
        self.data = "Parent Data"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.data = "Child Data"

obj = Child()
print(obj._Parent__data)   # ✅ Child Data
print(obj.data)  # ✅ Parent Data

"""
🔹 How Name Mangling Works
When a variable is declared with __ (double underscores) inside a class, Python automatically changes its name to:

 _ClassName__attribute
This prevents subclasses from accidentally overriding the variable.

🔹 Example of Name Mangling
"""
class Parent:
    def __init__(self):
        self.__private_var = 42  # Private attribute

obj = Parent()
# print(obj.__private_var)  # ❌ AttributeError

print(obj._Parent__private_var)  # ✅ Works (But not recommended)

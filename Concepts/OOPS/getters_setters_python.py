"""
Getters and Setters in Python
Getters and setters are methods used to access (get) and modify (set) the values of private attributes in a class.
In Python, they help encapsulate data and apply validation logic.

Why Use Getters and Setters?
✅ Encapsulation → Prevents direct access to sensitive data.
✅ Validation → Ensures valid data is set (e.g., salary cannot be negative).
✅ Flexibility → Allows modifying the internal logic without breaking the class interface.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    @property  # Getter
    def salary(self):
        return self.__salary

    @salary.setter  # Setter with validation
    def salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            raise ValueError("Salary must be positive!")

s1 = Employee('Rithesh', 30)
s1.salary = 50
print(s1._Employee__salary)

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
"""
🔹 Name Mangling in Inheritance
If a child class tries to declare a variable with the same name, it won't override the private variable in the parent class.
"""
class Parent:
    def __init__(self):
        self.__data = "Parent Data"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = "Child Data"

obj = Child()
print(obj._Child__data)   # ✅ Child Data
print(obj._Parent__data)  # ✅ Parent Data
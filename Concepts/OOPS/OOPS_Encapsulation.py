"""
 - Providing the controlled/restricted access to the attributes.
 - Achieved through Access Modifiers (public, private and protected members) and getters and setters
 - This involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit called a class.
 - Encapsulation is the process of hiding the internal state of an object and requiring all interactions to be performed through an object’s methods.
    - Provides better control over data.
    - Prevents accidental modification of data.
    - Promotes modular programming.

Access Modifiers:
 1) Public Members (No Underscore)
    Attributes and methods that can be accessed from anywhere.

 2) Protected Members (_Single Underscore)
    Indicates that an attribute/method should not be accessed directly but can still be accessed if needed.

 3) Private Members (__Double Underscore)
    Completely restricts direct access to attributes/methods.
"""

"""
Encapsulation with Getters & Setters:
 - To control access, we use getter and setter methods.
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private

    def get_salary(self):  # Getter
        return self.__salary

    def set_salary(self, new_salary):  # Setter
        if new_salary > 0:
            self.__salary = new_salary
        else:
            raise ValueError("Salary must be positive!")

emp = Employee("Rithesh", 50000)
# print(emp.get_salary())  # ✅ 50000
# emp.set_salary(60000)    # ✅ Updating salary
# print(emp.get_salary())  # ✅ 60000
# # emp.__salary = 70000  # ❌ This won't work due to encapsulation

# print(Employee('Rithesh', 50).__dict__)
print(emp.__dict__)
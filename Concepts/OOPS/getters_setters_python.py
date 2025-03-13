"""
Getters and Setters in Python
Getters and setters are methods used to access (get) and modify (set) the values of private attributes in a class. In Python, they help encapsulate data and apply validation logic.

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
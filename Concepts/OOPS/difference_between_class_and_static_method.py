"""
Difference Between Class Method and Static Method
In Python, class methods and static methods are special types of methods that serve different purposes.

🔹 Programming Perspective
Feature	Class Method (@classmethod)	Static Method (@staticmethod)
Decorator	                    @classmethod	                              @staticmethod
First Parameter	                cls (reference to the class itself)	          No implicit first parameter
Access to Class Variables?	    ✅ Yes, can modify class variables	          ❌ No access to class variables
Access to Instance (self)?	    ❌ No	                                      ❌ No
When to Use?	                When you need to work with class-level data	  When you don’t need class or instance data
Can Modify Class Attributes?	✅ Yes	                                      ❌ No

🔹 Real-World Use Cases
1️⃣ Class Method (@classmethod)
Used when we need to modify class-level attributes.
Use case: Suppose we want to keep track of the total number of students.
"""
class Student:
    total_students = 0  # Class variable

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1  # Updating class-level data

    @classmethod
    def get_total_students(cls):
        return f"Total Students: {cls.total_students}"

# Creating student objects
s1 = Student("Alice", 85)
s2 = Student("Bob", 90)

print(Student.get_total_students())  # ✅ "Total Students: 2"

"""
🔹 Real-World Example:

Bank Account System: A class method can be used to manage interest rates for all bank accounts.


2️⃣ Static Method (@staticmethod)
Used when we don’t need access to class or instance data.
Use case: Suppose we just want to validate marks without accessing instance or class data.
"""

class Student:
    @staticmethod
    def is_valid_marks(marks):
        return 0 <= marks <= 100  # No need for class or instance reference

# Calling static method
print(Student.is_valid_marks(85))  # ✅ True
print(Student.is_valid_marks(150)) # ❌ False

"""
🔹 Real-World Example:

Utility Functions: A static method in a logging system that formats log messages.
🔹 Key Takeaways
1️⃣ Class methods (@classmethod) modify class-level data.
2️⃣ Static methods (@staticmethod) are just utility functions that don’t interact with the class.
3️⃣ Use class methods for factory methods, modifying class attributes, and alternative constructors.
4️⃣ Use static methods for validations, utility functions, and calculations that don’t depend on class data.
"""
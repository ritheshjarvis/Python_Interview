"""
Class method:

 - A class method in Python is a method that's bound to the class rather than its instance.
 - It receives the class itself as its first argument (by convention named cls) rather than the instance (self).
 - Class methods are defined with the @classmethod decorator.

1. Alternative Constructors (Factory Methods)
Purpose: Provide different ways to create an instance.

2. Modifying or Accessing Class-Level Data
Purpose: Manage or update data that is shared across all instances.
-------------------------------------------------------------------------------------
Class variable:

 - Class variables are used when you want to store data that is shared across all instances of a class rather than data unique to each instance.
 - They are defined within a class but outside any instance methods.

1. Shared State:
When you have information that should be the same for every instance of a class. For example,
a counter to track how many instances of a class have been created.

2. Constants or Default Values:
Class variables can act as constants or default settings that every instance should have unless explicitly overridden.

3. Caching or Registries:
They can be used to cache results or maintain a registry of instances or configurations shared among all objects of that class.

4. Configuration Data:
When configuration options or settings apply to the entire class, not to individual objects.

Real world use case:
Bank Account System: A class method can be used to manage interest rates for all bank accounts.
"""
class Student:
    count: int = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Student.count = Student.count + 1

    @classmethod
    def student_with_email(cls, email: str):
        name = email.split('@')[0]
        return cls(name)

s1 = Student.student_with_email(3)

print(s1.name)
print(s1.count)

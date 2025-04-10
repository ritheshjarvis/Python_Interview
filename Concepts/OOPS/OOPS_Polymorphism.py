"""
Polymorphism in Python
Polymorphism means "many forms." In Python, it allows the same interface (method name) to be used for different types of objects.

1️⃣ Method Overriding (Runtime Polymorphism)
When a child class provides a specific implementation of a method already defined in its parent class.
Method Signature: The name of the method + the parameter list (types and order).

🔹 Example:
"""

class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):  # Overriding parent method
        print("Bark!")

class Cat(Animal):
    def make_sound(self):  # Overriding parent method
        print("Meow!")

# Common interface
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.make_sound()
"""
✅ Output:
Bark!
Meow!
Some generic animal sound

🔹 Real-World Example:
Think of a "Print" button that works differently for a PDF, Image, or Word file—each class provides its own print behavior.
-----------------------------------------------------------------------------------------------------
2️⃣ Method Overloading (Compile-Time Polymorphism)
Python does not support true method overloading (like Java), but you can achieve similar behavior using default arguments or *args and **kwargs.

🔹 Example using default arguments:
"""
class MathOperations:
    def add(self, a, b, c=0):  # Overloaded method (optional parameter)
        return a + b + c

math = MathOperations()
print(math.add(2, 3))      # Output: 5
print(math.add(2, 3, 4))   # Output: 9

# 🔹 Example using *args:

class MathOperations:
    def add(self, *numbers):
        return sum(numbers)

math = MathOperations()
print(math.add(2, 3))        # Output: 5
print(math.add(2, 3, 4, 5))  # Output: 14
"""
---------------------------------------------------------------------------------------------------
3️⃣ Operator Overloading
Python allows operators like +, -, *, etc., to be redefined for custom behavior in user-defined classes.

🔹 Example:
"""
class Box:
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):  # Overloading the '+' operator
        return Box(self.weight + other.weight)

    def __str__(self):
        return f"Box weight: {self.weight} kg"

box1 = Box(10)
box2 = Box(20)
box3 = box1 + box2  # Uses __add__ method

print(box3)  # Output: Box weight: 30 kg
"""
✅ Real-World Example:
Imagine adding two bank accounts and getting a new account with their combined balance.

4️⃣ Duck Typing (Dynamic Polymorphism)
In Python, we don’t care about the type of an object, only whether it has the expected methods and behavior.
"If it walks like a duck and quacks like a duck, it's a duck!"

🔹 Example:
"""
class Bird:
    def fly(self):
        print("Flying in the sky!")

class Airplane:
    def fly(self):
        print("Flying using jet engines!")

# Common interface
def take_off(entity):
    entity.fly()

take_off(Bird())     # Output: Flying in the sky!
take_off(Airplane()) # Output: Flying using jet engines!
"""
✅ Real-World Example:
Any payment system (PayPal, Stripe, Razorpay) should have a process_payment() method, even though their implementations differ.
"""

"""
Why Real Method Overloading is Not Possible in Python?
1) Lack of static method signature
2) Python functions don’t enforce strict type checking.
"""
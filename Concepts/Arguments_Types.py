"""
1. Positional Arguments:
These are the simplest type of arguments. When you call a function, the values you pass are matched with the
function’s parameters by their order (position).
"""

def add(a, b, c):
    return a + b + c

# Positional arguments: 1 goes to a, 2 goes to b, and 3 goes to c.
print(add(1, 2, 3))  # Output: 6

"""
2. Default (or Optional) Arguments:
You can assign a default value to one or more parameters in the function definition. 
These values are used if the caller does not provide them. Default arguments must come after 
any non-default (required) arguments. 
"""

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Uses default greeting: "Hello, Alice!"
greet("Bob", greeting="Hi") # Overrides default: "Hi, Bob!"

"""
3. Keyword Arguments:
Instead of relying on the order of the arguments, you can specify arguments by the parameter
name during a function call. This improves readability and allows you to pass arguments in any order.
"""

def student_info(name, age, grade):
    print(f"{name} is {age} years old and in {grade} grade.")

# Keyword arguments can be passed in any order:
student_info(age=12, name="Charlie", grade="7th")
When mixing positional and keyword arguments in a function call, all positional arguments must come before any keyword arguments.

"""
4. Arbitrary Positional Arguments (*args):
If you want to create a function that can accept a variable (and unknown) number of positional arguments, 
you can use the *args syntax. Inside the function, *args is treated as a tuple of all the extra positional arguments.
"""

def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3)  # Prints 1, 2, 3 each on a new line

"""
5. Arbitrary Keyword Arguments (**kwargs):
Similarly, if you want to accept any number of keyword (named) arguments, you can use **kwargs. Inside the function,
**kwargs is a dictionary where the keys are the argument names and the values are the corresponding values.
"""

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Dana", age=20, city="New York")
# Output:
# name: Dana
# age: 20
# city: New York

"""
Summary:
1. Positional Arguments: Matched by order.
2. Default Arguments: Provide fallback values if not specified; they must follow required arguments.
3. Keyword Arguments: Passed by name; allow you to specify arguments out of order.
4. Arbitrary Positional Arguments (*args): Gather extra positional arguments into a tuple.
5. Arbitrary Keyword Arguments (**kwargs): Gather extra keyword arguments into a dictionary.
6. Positional-Only / Keyword-Only: Newer features (Python 3.8+) that let you enforce how arguments are passed.
"""

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
# When mixing positional and keyword arguments in a function call, all positional arguments must come before any keyword arguments.

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

"""
6. Positional-Only and Keyword-Only Arguments (Advanced):
Starting in Python 3.8, you can specify that some parameters must be passed by position only 
(using a / in the parameter list) or by keyword only (by placing a * before them).
"""

# Positional-only parameters:

def func(a, b, /, c, d):
    # a and b can only be passed positionally; c and d can be positional or keyword.
    print(a, b, c, d)

func(1, 2, 3, 4)            # Valid.
# func(a=1, b=2, c=3, d=4)   # Error: a and b cannot be passed by keyword.

"""
7. using * (asterisk)
a and b → Positional arguments (must be passed in order).

c and d → Keyword-only arguments (must be passed using explicit keywords).

* (asterisk) → Forces all arguments after it (c, d) to be keyword-only.

"""
# Keyword-only parameters:

def func(a, b, *, c, d):
    # c and d must be passed as keyword arguments.
    print(a, b, c, d)

func(1, 2, c=3, d=4)  # Valid.
# func(1, 2, 3, 4)   # Error: c and d must be specified with keywords.

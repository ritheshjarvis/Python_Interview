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

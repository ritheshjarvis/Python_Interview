"""
 - A lambda function in Python is a small, anonymous function defined using the lambda keyword instead of def.
 - It's generally used for short, throwaway functions and consists of a single expression.

 Syntax:
 function_name = lambda arguments: expression

"""


# Regular function
def add(a, b):
    return a + b

# Lambda function
add = lambda x, y: x + y

print(add(1, 2))

def square(x):
    return x * x

# Lambda Function
square = lambda x: x*x

numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]

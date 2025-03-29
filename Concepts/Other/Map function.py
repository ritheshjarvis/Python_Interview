"""
map() Function in Python
The map() function in Python is used to apply a function to each item in an iterable (like a list, tuple, etc.) and return an iterator with the transformed values.

🔹 Syntax:
    map(function, iterable)
    function: The function to apply to each element.

iterable: The sequence (list, tuple, etc.) whose elements will be processed.

🔹 It returns an iterator, so you need to convert it to a list or tuple to see the results.
"""

#  Using map() to Convert Data Types
num_strings = ["10", "20", "30"]
numbers = list(map(int, num_strings))  # Convert list of strings to integers
print(numbers)  # Output: [10, 20, 30]

# Using map() with str.upper()
words = ["hello", "world"]
uppercase_words = list(map(str.upper, words))
print(uppercase_words)  # Output: ['HELLO', 'WORLD']

# Alternative: List Comprehension vs. map()
# Using map()
squared_map = list(map(lambda x: x**2, numbers))

# Using list comprehension (alternative)
squared_list = [x**2 for x in numbers]

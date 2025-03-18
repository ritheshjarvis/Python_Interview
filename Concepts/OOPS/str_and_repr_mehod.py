class Box:
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):  # Overloading the '+' operator
        return Box(self.weight + other.weight)

    # __str__() → For end-users, should be user-friendly
    # Priority 1
    # print(str(obj))
    def __str__(self): # Priority 1
        return f"Box weight: {self.weight} kg"

    # For developers, should return a valid Python exp that can recreate the object.
    # Priority 2
    # print(repr(obj))
    def __repr__(self): # Priority 2
        return f'Box({self.weight})'
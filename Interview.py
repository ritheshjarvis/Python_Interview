class Example:
    def __init__(self, number):
        self.number = number

    def __call__(self):
        return self.number * 2


ex1 = Example(5)
print(ex1())


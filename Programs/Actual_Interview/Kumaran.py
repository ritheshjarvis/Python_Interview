dict_input = [{'id': 1, 'subjects': {'maths': 90, 'science': 75}}, ]

# Generate a Dictionary

class Dictionary:
    id = 0

    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks
        Dictionary.id += 1
        self.output = {'subjects': {self.subject, self.marks}}

    def add_subject(subject, marks):
        self.out

    def return_output(self):
        return {'id': id, self.output}


d1 = Dictionary('xyz', 70)

# string slicing code

input_ = 'rithesh'

print(input_[::-1])
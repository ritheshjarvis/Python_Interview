"""
Abstract Classes in Python:
✅ A class is an abstract class if it contains at least one abstract method (a method declared but not implemented).
✅ Even if the class has concrete (regular) methods, it will still be an abstract class as long as it has at least one abstract method.
✅ Abstract classes cannot be instantiated directly.

Interface in Python:
In Python, an interface is just an abstract class where all methods are abstract (i.e., it contains no concrete methods).
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def walk(self):
        print("walk")


class Tiger(Animal):

    def sound(self):
        print("Tiger sound")

t = Tiger()
t.sound()
t.walk()

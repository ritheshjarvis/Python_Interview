"""
Iterarator is an object that allows you to traverse elements of a Collection(like list, set, type, dict, string etc) one at a time,
without needing to know how the Collection structured internally.

Key points about an Iterator:

1. Iterator Protocol → An object is called an iterator if it implements two methods:

    __iter__() → returns the iterator object itself.

    __next__() → returns the next value from the sequence. If no more elements are left, it raises a StopIteration exception.

2. Iterators are stateful → they remember their current position, so each call to next() gives you the next element.

3. All iterable objects (like lists, tuples, sets) can produce an iterator using the built-in iter() function.
"""

# A normal list (iterable, but not an iterator itself)
numbers = [10, 20, 30]

# Get iterator from the list
it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
print(next(it))  # Raises StopIteration


"""
Iterator vs Iterable

    Iterable → An object that can return an iterator (list, tuple, dict, set, str).

    Iterator → The object that actually yields elements one by one (iter(list) returns an iterator).

👉 So, in simple words:

    An iterable is like a book (you can go through it).

    An iterator is like a bookmark (it remembers where you left off and lets you continue).

"""
nums = [1, 2, 3]
print(hasattr(nums, "__iter__"))     # True (list is iterable)
print(hasattr(nums, "__next__"))     # False (list itself is not an iterator)

it = iter(nums)
print(hasattr(it, "__iter__"))       # True (iterator is iterable)
print(hasattr(it, "__next__"))       # True (iterator has __next__)

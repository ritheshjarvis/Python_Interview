"""
1. Always do the try and catch block at the very outer scope
2. In all other places try to raise the Exceptions
"""

"""
✅ 1. Try/Except Block at the Outer Scope (e.g., main or controller layer)
Best Practice:
Wrap your main logic, or entry point, in a try/except block to gracefully handle uncaught exceptions and give clean feedback (logs, error messages, alerts, etc.).

Why:
You want to centralize exception handling and avoid repetitive try/except everywhere. The outer block is the best place to log the error, show meaningful messages, or exit gracefully.

def main():
    result = process_file("input.txt")
    print(result)

try:
    main()
except Exception as e:
    print(f"Something went wrong: {e}")

✅ 2. Raise Exceptions in Inner Logic (i.e., in lower-level functions)
Best Practice:
Instead of catching exceptions in every function, you should raise meaningful exceptions when something goes wrong. This lets the outer scope (or the caller) decide how to handle it.

Why:
It improves modularity, testability, and separates error detection from error handling.

def process_file(path):
    if not path.endswith(".txt"):
        raise ValueError("Only .txt files are supported")

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    # Continue processing
🔥 Real-World Analogy
Think of a system where:

Functions are workers – they just raise flags (errors).

Main function is the manager – it handles the issues and decides what to do (retry, report, log, etc.).

🧠 Bonus Tip
You can also define custom exceptions for more clarity:

class InvalidFileTypeError(Exception):
    pass
"""


import os

path = r'C:\Rithesh_B\Projects\Behav'

def print_path(path):
    # try:
    if not os.path.exists(path):
        raise FileNotFoundError("File missing") from e
    # except Exception as e:
    #     print(f'>>> {e}')

    print("function control here")


try:
    print_path(path)
    print("Control here")
except Exception as e:
    print(f'=== {e}')

print("----------------------------------------")

def add(a,b):
    raise AttributeError

def sum():
    a = add
    try:
        print(a(10,20))

    except Exception as e:
        raise AttributeError
        # print("Excpetion Occurred")
        # raise e
        # pass

try:
    sum()
except Exception as e:
    print("Final Exception")
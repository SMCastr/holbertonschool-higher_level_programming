#!/usr/bin/python3
""" Module for class to JSON function
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.
    """
    return obj.__dict__

# Sample usage for testing
if __name__ == "__main__":
    class MyClass:
        def __init__(self, name):
            self.name = name
            self.number = 0

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

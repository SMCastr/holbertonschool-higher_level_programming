#!/usr/bin/python3

def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object for which attributes and methods should be looked up.

    Returns:
        A list of strings representing attributes and methods of the object.
    """
    return dir(obj)

#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("An exception was raised")
    except TypeError as te:
        print("Exception raised")
        raise te

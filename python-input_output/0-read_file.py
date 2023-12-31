#!/usr/bin/python3
""" Input/Output Module"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end="")

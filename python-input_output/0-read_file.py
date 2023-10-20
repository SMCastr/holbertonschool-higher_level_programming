#!/usr/bin/python3

def read_file(filename=""):
    """Read a text file and print its content to stdout.

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")

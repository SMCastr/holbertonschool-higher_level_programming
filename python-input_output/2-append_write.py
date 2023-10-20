#!/usr/bin/python3

def append_write(filename="", text=""):
    """Append a string to the end of a text file and return the number of characters added.

    Args:
        filename (str): The name of the text file to append to.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)

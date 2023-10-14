#!/usr/bin/python3
"""
Module to print text with indentation
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    special_chars = [".", "?", ":"]
    for char in text:
        if char in special_chars:
            print(char)
            print()
        else:
            print(char, end="")

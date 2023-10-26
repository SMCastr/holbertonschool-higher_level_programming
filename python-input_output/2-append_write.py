#!/usr/bin/python3
"""Module for append_write"""""


def append_write(filename="", text=""):
    """Append a string to the end of a text file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)

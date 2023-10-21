#!/usr/bin/python3
"""
This module defines a function to create an object from a JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object loaded from the JSON file.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        json.JSONDecodeError: If the JSON string is invalid.
    """
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    # Example usage and test cases
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except FileNotFoundError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except json.JSONDecodeError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

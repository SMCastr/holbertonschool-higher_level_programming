#!/usr/bin/python3

import json

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    :param filename: The name of the JSON file to load.
    :return: The Python object represented by the JSON data in the file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

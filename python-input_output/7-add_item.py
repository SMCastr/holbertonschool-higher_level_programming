#!/usr/bin/python3

import json

def load_add_save(filename, args):
    """Load a list from a JSON file, add new elements, and save it back to the file.

    Args:
        filename (str): The name of the JSON file to read and update.
        args (list): A list of strings to add to the loaded list.

    Returns:
        None
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.extend(args)

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)

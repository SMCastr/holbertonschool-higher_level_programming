#!/usr/bin/python3

import json

def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.

    Args:
        my_obj: The Python object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)

if __name__ == "__main__":
    # Additional test cases

    # List containing various data types
    data = [1, 2, 3, "Holberton"]
    s_data = to_json_string(data)
    print(s_data)

    # Empty list
    data = []
    s_data = to_json_string(data)
    print(s_data)

    # Dictionary
    data = {'id': 12, 'numbers': [1, 2, 4]}
    s_data = to_json_string(data)
    print(s_data)

    # Large dictionary
    data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
        'key4': 'value4',
        'key5': 'value5',
        'key6': 'value6',
    }
    s_data = to_json_string(data)
    print(s_data)

    # List of dictionaries
    data = [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Alice'},
        {'id': 3, 'name': 'Bob'},
    ]
    s_data = to_json_string(data)
    print(s_data)

    # String
    data = "Simple string"
    s_data = to_json_string(data)
    print(s_data)

    # Invalid data - dictionary with mixed data types
    data = {'id': 3, 'title': 'Holberton', 'number': 89}
    try:
        s_data = to_json_string(data)
        print(s_data)
    except TypeError as e:
        print(f"[{e.__class__.__name__}] {e}")

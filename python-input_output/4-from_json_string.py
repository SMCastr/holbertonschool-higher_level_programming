#!/usr/bin/python3

import json

def from_json_string(my_str):
    """
    Return an object represented by a JSON string.

    Args:
        my_str (str): A JSON string.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

if __name__ == "__main__":
    # Example usage and test cases
    s_data = "[1, 2, 3, \"Holberton\"]"
    data = from_json_string(s_data)
    print(data)
    print(type(data))

    s_data = "[]"
    data = from_json_string(s_data)
    print(data)
    print(type(data))

    s_data = "{ 'id': 12 }"
    data = from_json_string(s_data)
    print(data)
    print(type(data))

    s_data = "{ 'id': 12, 'numbers': [1, 2, 4] }"
    data = from_json_string(s_data)
    print(data)
    print(type(data))

    s_data = """{
        "name": "John",
        "places": ["San Francisco", "Tokyo"],
        "id": 12,
        "info": {
            "average": 3.14,
            "age": 36
        },
        "is_active": true
    }"""
    data = from_json_string(s_data)
    print(data)
    print(type(data))

    s_data = """[
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]"""
    data = from_json_string(s_data)
    print(data)
    print(type(data))

    s_data = '"Simple string"'
    data = from_json_string(s_data)
    print(data)
    print(type(data))

    s_data = """{ 'id': 12, 'num': 4, 'holberton' }"""
    try:
        data = from_json_string(s_data)
        print(data)
        print(type(data))
    except json.JSONDecodeError as e:
        print(e)


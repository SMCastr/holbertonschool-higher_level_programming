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
    # Additional test case
    my_set = {132, 3}
    try:
        s_my_set = to_json_string(my_set)
        print(s_my_set)
        print(type(s_my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

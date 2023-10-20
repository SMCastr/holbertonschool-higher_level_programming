import json

def to_json_string(my_obj):
    """Convert a Python data structure to a JSON string.

    Args:
        my_obj: The Python data structure to be converted to JSON.

    Returns:
        str: The JSON representation of the input object.
    """
    return json.dumps(my_obj)

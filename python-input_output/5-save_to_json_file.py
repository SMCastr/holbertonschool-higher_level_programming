import json

def save_to_json_file(my_obj, filename):
    """Write an object to a text file in JSON format.

    Args:
        my_obj: The Python object to be saved to the file.
        filename (str): The name of the text file to save the object to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

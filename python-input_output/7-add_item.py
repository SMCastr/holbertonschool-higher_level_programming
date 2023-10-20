#!/usr/bin/python3
import sys
import os

# Check if the add_item.json file exists
if os.path.exists("add_item.json"):
    # If it exists, load the existing list from the file
    from load_from_json_file import load_from_json_file
    my_list = load_from_json_file("add_item.json")
else:
    # If it doesn't exist, create an empty list
    my_list = []

# Append the command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list as a JSON representation in add_item.json
from save_to_json_file import save_to_json_file
save_to_json_file(my_list, "add_item.json")

#!/usr/bin/python3
"""Module for add_item"""


import sys
import os

if os.path.exists("add_item.json"):
    from load_from_json_file import load_from_json_file
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

my_list.extend(sys.argv[1:])

from save_to_json_file import save_to_json_file
save_to_json_file(my_list, "add_item.json")

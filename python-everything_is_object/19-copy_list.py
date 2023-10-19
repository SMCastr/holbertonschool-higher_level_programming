#!/usr/bin/python3

def copy_list(a_list):
    return a_list.copy()

# Test cases
test_cases = [
    [1, 2, 3],
    [1],
    [1, "2", 3],
    [1, [2, 3], {'id': 12}],
    []
]

for my_list in test_cases:
    print(f"Original List: {my_list}")
    new_list = copy_list(my_list)
    print(f"Copied List: {new_list}")
    print(f"Is Copied List Equal: {new_list == my_list}")
    print(f"Is Copied List Identical: {new_list is my_list}")

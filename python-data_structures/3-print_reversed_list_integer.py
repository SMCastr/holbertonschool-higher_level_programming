#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    result = []
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
        if my_list[i] % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result


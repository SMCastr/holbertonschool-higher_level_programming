#!/usr/bin/python3
for first in range(0, 10):
    for second in range(0, 10):
        if first == 8 and second == 9:
            print("{}{}".format(first, second))
        elif first < second:
            print("{}{}, ".format(first, second), end="")
        else:
            continue
        
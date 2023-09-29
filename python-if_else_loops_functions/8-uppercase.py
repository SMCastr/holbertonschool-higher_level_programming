#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            offset = ord('a')
            print("{}".format(chr(ord(char) - offset + ord('A'))), end="")
        else:
            print("{}".format(char), end="")
    print()

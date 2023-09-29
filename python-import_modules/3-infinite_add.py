#!/usr/bin/python3
import sys

args = sys.argv[1:]
sum_result = 0

for arg in args:
    sum_result += int(arg)

print(sum_result)

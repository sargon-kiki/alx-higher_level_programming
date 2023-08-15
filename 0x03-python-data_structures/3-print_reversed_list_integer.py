#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reversed order."""
    is_list = isinstance(my_list, list)
    if is_list:
        my_list.reverse()
        for item in my_list:
            print("{:d}".format(item))

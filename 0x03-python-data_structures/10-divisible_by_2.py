#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list with truthy."""
    truthy_list = []
    for item in my_list:
        if item % 2 == 0:
            truthy_list.append(True)
        else:
            truthy_list.append(False)
    return truthy_list

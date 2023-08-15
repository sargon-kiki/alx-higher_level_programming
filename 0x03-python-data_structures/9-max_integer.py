#!/usr/bin/python3
# 9-max_integer.py
def max_integer(my_list=[]):
    """Find the max integer or number of a list."""
    if not my_list:
        return None
    max_num = my_list[0]
    for i in my_list:
        if i > max_num:
            max_um = i
    return max_num

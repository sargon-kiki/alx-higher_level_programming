#!/usr/bin/python3
# 2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    valid_length = len(my_list) - 1
    if idx < 0:
        return my_list
    if idx > valid_length:
        return my_list
    my_list[idx] = element
    return my_list

#!/usr/bin/python3
# 1-search_replace.py


def search_replace(my_list, search, replace):
    """Search and replace"""
    new_list = my_list[::]
    for idx, item in enumerate(new_list):
        if item == search:
            new_list[idx] = replace
    return new_list

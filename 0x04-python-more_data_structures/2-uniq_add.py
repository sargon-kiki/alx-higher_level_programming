#!/usr/bin/python3
# 2-uniq_add.py
def uniq_add(my_list=[]):
    """Add all unique integers"""
    uniq_list = set(my_list)
    total = 0
    for item in uniq_list:
        total += item
    return total

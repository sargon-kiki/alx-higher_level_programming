#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """ Delete an item in list"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list

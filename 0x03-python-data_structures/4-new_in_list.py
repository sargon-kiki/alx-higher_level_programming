#!/usr/bin/python3
# 4-new_in_list.py
def new_in_list(my_list, idx, element):
    """New inplace list"""
    m_list = [item for item in my_list]
    valid_length = len(my_list) - 1
    if idx < 0:
        return my_list
    if idx > valid_length:
        return my_list
    m_list[idx] = element
    return m_list

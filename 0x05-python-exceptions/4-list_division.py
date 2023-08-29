#!/usr/bin/python3
# 4-list_division.py


def list_division(my_list_1, my_list_2, list_length):
    """Division of list
    Args:
        my_list_1 : first list
        my_list_2: second list
        list_length: length to use for div
    Returns:
        A new list of of results from division
    """
    div_list = []
    div_result = 0
    for index in range(0, list_length):
        try:
            div_result = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            div_list.append(div_result)
    return div_list

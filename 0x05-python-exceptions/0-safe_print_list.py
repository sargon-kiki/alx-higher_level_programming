#!/usr/bin/python3
# 0-safe_print_list.py


def safe_print_list(my_list=[], x=0):
    """Print x number elements in list with exception handle

    Args:
        my_list (list): list to print
        x (int) : number of elements to print

    Returns:
        The number of elements printed
    """
    elem_counter = 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            elem_counter += 1
        except IndexError:
            break
    print("")
    return elem_counter

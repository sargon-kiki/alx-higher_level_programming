#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Remove all characters c and C from a string."""
    co_string = "".join(
        [letter for letter in my_string if letter != "C" and letter != "c"]
    )
    return co_string

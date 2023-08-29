#!/usr/bin/python3
# 100-safe_print_integer_err.py

import sys


def safe_print_integer_err(value):
    """Safe print an integer

    Args:
        value (int) : Integer to print
    Returns:
        if error False else True
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False

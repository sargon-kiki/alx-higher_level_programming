#!/usr/bin/python3
# 1-safe_print_integer.py


def safe_print_integer(value):
    """Print an integer with {:d}
    Args:
        value (int): The integer to print.
    Returns:
        False when error else True

    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

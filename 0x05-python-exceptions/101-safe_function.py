#!/usr/bin/python3
# 101-safe_function.py

import sys


def safe_function(fct, *args):
    """handling exceptions in func exec

    Args:
        fct: function to exec
        args: arguments to functions
    Returns:
        None when error occurs else value
    """
    try:
        result = fct(*args)
        return result
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None

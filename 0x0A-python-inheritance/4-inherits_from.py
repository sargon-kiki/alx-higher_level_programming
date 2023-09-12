#!/usr/bin/python3
# 4-inherits_from.py

"""My definition an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if it checks out.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) or type(obj) != a_class:
        return True
    return False

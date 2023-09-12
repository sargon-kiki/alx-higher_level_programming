#!/usr/bin/python3
# 1-my_list.py

"""Defines an inherited list class MyList."""


class MyList(list):
    """Subclass builtin class"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

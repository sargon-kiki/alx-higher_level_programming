#!/usr/bin/python3
# 6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    ordered_keys = list(a_dictionary.keys())
    ordered_keys.sort()
    for key in ordered_keys:
        print(f"{key}: {a_dictionary[key]}")

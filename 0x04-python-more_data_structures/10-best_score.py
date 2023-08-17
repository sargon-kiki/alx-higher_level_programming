#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    """Returns a key with the biggest value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    key = list(a_dictionary.keys())[0]
    max_val = a_dictionary[key]
    for k, v in a_dictionary.items():
        if v > max_val:
            max_val = v
            key = k
    return max_val

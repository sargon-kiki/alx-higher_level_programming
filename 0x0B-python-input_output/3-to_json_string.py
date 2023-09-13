#!/usr/bin/python3
# 3-to_json_string.py

"""Defs a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON rep of a string object."""
    return json.dumps(my_obj)

#!/usr/bin/python3
# 5-save_to_json_file.py

"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON rep."""
    with open(filename, "w") as fb:
        json.dump(my_obj, fb)

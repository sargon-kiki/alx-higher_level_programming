#!/usr/bin/python3
# 6-load_from_json_file.py

"""Defs a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as fb:
        return json.load(fb)

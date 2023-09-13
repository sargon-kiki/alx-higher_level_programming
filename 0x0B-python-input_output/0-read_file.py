#!/usr/bin/python3
# 0-read_file.py

"""Defs a text file-reading function."""


def read_file(filename=""):
    """Print contents text file to stdout."""
    with open(filename, encoding="utf-8") as fb:
        print(fb.read(), end="")

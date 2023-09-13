#!/usr/bin/python3
# 1-write_file.py

"""Defs a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The num of characters written.
    """
    with open(filename, "w", encoding="utf-8") as fb:
        return fb.write(text)

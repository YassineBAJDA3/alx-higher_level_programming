#!/usr/bin/python3
"""Defining write_file with 2 args"""


def write_file(filename="", text=""):
    """
    Writes a string to text file (UTF-8 encoded)
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

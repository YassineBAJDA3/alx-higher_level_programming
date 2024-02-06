#!/usr/bin/python3
"""Defining a function that takes two parameters"""


def append_write(filename="", text=""):
    """
    appending a string at the end of text file (UTF-8 encoded)
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

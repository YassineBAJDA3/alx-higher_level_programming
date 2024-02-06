#!/usr/bin/python3
"""defining a read_file function"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8 encoded)
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

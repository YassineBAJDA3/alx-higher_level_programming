#!/usr/bin/python3
"""defining append_file with two arguments"""


def write_file(filename="", text=""):
    """append to file_name with UTF8"""
    with open(filename, "a", encoding='UTF8') as file:
        return file.write(text)

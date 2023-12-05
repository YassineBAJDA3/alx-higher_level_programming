#!/usr/bin/python3
"""defining write_file with two arguments"""


def write_file(filename="", text=""):
    """reads file_name with UTF8"""
    with open(filename, "w", encoding='UTF8') as file:
        return file.write(text)

#!/usr/bin/python3
"""defining read_file functin"""


def read_file(filename=""):
    """reads file_name with UTF8"""
    with open(filename, encoding = 'UTF8') as file:
        print(file.read(), end="")

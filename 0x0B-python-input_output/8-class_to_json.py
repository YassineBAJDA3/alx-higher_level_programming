#!/usr/bin/python3
"""contain the "class_to_json" function"""


def class_to_json(obj):
    """return the dictionary description with qimle data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    return obj.__dict__

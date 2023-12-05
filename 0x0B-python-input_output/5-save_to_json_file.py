#!/usr/bin/python3
"""difining save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """write an object to text file"""
    with open(filename, 'w', encoding="UTF8") as file:
        json.dump(my_obj, file)

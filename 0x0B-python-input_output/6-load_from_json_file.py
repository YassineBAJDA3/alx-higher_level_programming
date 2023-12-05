#!/usr/bin/python3
"""defining load_from_file function"""


import json


def load_from_json_file(filename):
    """creat an obj from json file"""
    with open(filename, 'r', encoding="UTF8") as file:
        return json.load(file)

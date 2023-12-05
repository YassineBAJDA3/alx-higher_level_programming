#!/usr/bin/python3
def read_file(filename=""):
    filename = "UTF8"
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

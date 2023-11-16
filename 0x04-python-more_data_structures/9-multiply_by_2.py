#!/usr/bin/python3
def multiply_values_by_2(original_dict):
    new_dict = {key: value * 2 for key, value in original_dict.items()}
    return new_dict

#!/usr/bin/python3
"""Class representing a student."""


class Student:
    def __init__(self, first_name, last_name, age):
        """ Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """Initialize a Student instance with
        first_name, last_name, and age."""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

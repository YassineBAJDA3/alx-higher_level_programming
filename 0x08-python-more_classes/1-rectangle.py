#!/usr/bin/python3
"""
Defining an empty class Rectangle
"""
class Rectangle:
    """Representation of Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for he private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0 :
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def width(self):
        """getter for the private instance attribute height"""
        return self.__height
    
    @width.setter
    def width(self, value):
        """setter for he private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0 :
            raise ValueError("height must be >= 0")
        self.__height = value

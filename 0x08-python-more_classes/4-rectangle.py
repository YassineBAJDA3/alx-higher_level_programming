#!/usr/bin/python3
"""
Defining a class Rectangle with custom string representation
"""

class Rectangle:
    """Representation of Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """String representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        
        return rectangle_str.rstrip('\n')
    def __repr__(self):
        """String representation to recreate the object using eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

#!/usr/bin/python3

class Square:
    """Defines a Square."""

    def __init__(self, size=0):
        """Initialize the Square object with the provided size."""
        self.size = size  # Calls the size property setter
    
    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size of the square with type and value verification."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

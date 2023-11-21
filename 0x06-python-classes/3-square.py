#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a Square."""

    def __init__(self, size=0):
        """Initialize the Square object with the provided size."""
        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Check if size is non-negative
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Assign the validated size to the instance attribute

        def area(self):
            """Calculate and return the area of the square."""
            return self.__size ** 2

#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square with equal width and height,
    inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

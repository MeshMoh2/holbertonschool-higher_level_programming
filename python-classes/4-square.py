#!/usr/bin/python3
"""
This module defines a class Square with size getter and setter.
"""


class Square:
    """Represents a square with property access for size."""

    def __init__(self, size=0):
        """
        Initialize the square with size validation.

        Args:
            size (int): Size of the square, must be >= 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size with validation.

        Args:
            value (int): New size.

        Raises:
            TypeError: If value is not int.
            ValueError: If value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area.
        """
        return self.__size ** 2

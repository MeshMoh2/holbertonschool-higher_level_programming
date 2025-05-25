#!/usr/bin/python3
"""
This module defines a class Square that can compute area.
"""


class Square:
    """Represents a square with size and area calculation."""

    def __init__(self, size=0):
        """
        Initialize the square with size validation.

        Args:
            size (int): Size of the square, must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2

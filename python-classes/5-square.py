#!/usr/bin/python3
"""
This module defines a class Square that prints itself with '#'.
"""


class Square:
    """Represents a square with printable output."""

    def __init__(self, size=0):
        """
        Initialize the square with size validation.

        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): Size to set.

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

    def my_print(self):
        """
        Print the square using '#' or an empty line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

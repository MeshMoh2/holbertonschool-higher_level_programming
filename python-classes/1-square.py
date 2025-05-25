#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute.
"""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """
        Initialize the square.

        Args:
            size (int): The size of the square (not validated).
        """
        self.__size = size

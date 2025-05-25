#!/usr/bin/python3
"""
This module defines a class Square with position and print offset.
"""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize square with size and position.

        Args:
            size (int): Size of the square.
            position (tuple): Position tuple (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: Size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size with validation.

        Args:
            value (int): Size.

        Raises:
            TypeError: If value not int.
            ValueError: If value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: Position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set position with validation.

        Args:
            value (tuple): Position (x, y).

        Raises:
            TypeError: If value not a tuple of 2 positive ints.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(v, int) and v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate area.

        Returns:
            int: The area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print square using position and size.
        """
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

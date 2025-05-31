#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using width and height,
    with validation and area calculation.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Args:
            width (int): The rectangle's width.
            height (int): The rectangle's height.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: Area computed as width * height.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

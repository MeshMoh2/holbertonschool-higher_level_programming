#!/usr/bin/env python3
"""
This module defines an abstract Shape class and
concrete Circle and Rectangle classes that implement area and perimeter.
It also provides a function to print shape information using duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """Calculate area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Circle class implementing Shape interface.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class implementing Shape interface.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.

    Args:
        shape: An object that implements area() and perimeter()
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

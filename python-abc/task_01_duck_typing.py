#!/usr/bin/env python3
"""
Defines an abstract base class Shape and two implementations: Circle and Rectangle.
Includes shape_info() to demonstrate duck typing by calling area and perimeter methods.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """A circle shape defined by its radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """A rectangle shape defined by width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of any object implementing area and perimeter methods.
    Demonstrates duck typing.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

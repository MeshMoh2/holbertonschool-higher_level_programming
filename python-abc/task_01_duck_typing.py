#!/usr/bin/env python3
"""
Duck typing with abstract shapes: Circle and Rectangle.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """A circle with a given radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """A rectangle defined by its width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Prints area and perimeter using duck typing."""
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")

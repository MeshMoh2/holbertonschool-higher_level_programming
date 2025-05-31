#!/usr/bin/env python3
"""
This module defines a Shape interface using abstract base classes,
and implements Circle and Rectangle with duck typing demonstration.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    Circle shape, defined by its radius.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Returns the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape, defined by width and height.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape.

    Args:
        shape: An object expected to have area() and perimeter() methods.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

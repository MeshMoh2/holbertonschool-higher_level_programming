#!/usr/bin/python3
"""
This module defines abstract and concrete shape classes.
It demonstrates the use of abstract base classes and duck typing
by enforcing a common interface for calculating area and perimeter.
"""

# ABC module provides the base for abstract class declarations
from abc import ABC, abstractmethod
# math module is used to calculate circle-related geometry
import math


class Shape(ABC):
    """
    Abstract base class for all shape types.
    Defines required methods for calculating area and perimeter.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        Returns:
            float: The computed area.
        """
        pass  # To be implemented by subclasses

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        Returns:
            float: The computed perimeter.
        """
        pass  # To be implemented by subclasses


class Circle(Shape):
    """
    Circle shape class implementing required Shape interface.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a specific radius.
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius  # Store radius for area and perimeter calculation

    def area(self):
        """
        Compute the area of the circle.
        Returns:
            float: Area of the circle.
        """
        return math.pi * self.radius ** 2  # Use pi * r^2 formula

    def perimeter(self):
        """
        Compute the perimeter of the circle.
        Returns:
            float: Perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius  # Use 2 * pi * r formula


class Rectangle(Shape):
    """
    Rectangle shape class implementing required Shape interface.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.
        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width  # Set width
        self.height = height  # Set height

    def area(self):
        """
        Compute the area of the rectangle.
        Returns:
            float: Area of the rectangle.
        """
        return self.width * self.height  # Use width * height formula

    def perimeter(self):
        """
        Compute the perimeter of the rectangle.
        Returns:
            float: Perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)  # Use 2 * (w + h) formula


def shape_info(shape):
    """
    Print area and perimeter of any object with area and perimeter methods.
    Demonstrates duck typing in Python.
    Args:
        shape (object): Any object with area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))  # Print area
    print("Perimeter: {}".format(shape.perimeter()))  # Print perimeter

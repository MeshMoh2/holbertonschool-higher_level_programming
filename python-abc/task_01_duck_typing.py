#!/usr/bin/python3
"""
This module defines abstract and concrete shape classes
demonstrating abstract base classes and duck typing in Python.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
"""
 Abstract base class for all shapes.
 Defines a common interface for calculating area and perimeter.
 """

    @abstractmethod
    def area(self):
"""
Calculate the area of the shape.
Returns:
float: The area of the shape.
"""
        pass

    @abstractmethod
    def perimeter(self):
"""
Calculate the perimeter of the shape.
Returns:
float: The perimeter of the shape.
"""
        pass


class Circle(Shape):
"""
Circle shape class implementing area and perimeter.
"""

    def __init__(self, radius):
"""
Initialize a Circle with a radius.
Args:
radius (float): The radius of the circle.
"""
        self.radius = radius

    def area(self):
"""
Calculate the area of the circle.
Returns:
float: Area of the circle.
"""
        return math.pi * self.radius ** 2

    def perimeter(self):
"""
Calculate the perimeter of the circle.
Returns:
float: Perimeter of the circle.
"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
"""
Rectangle shape class implementing area and perimeter.
"""

    def __init__(self, width, height):
"""
Initialize a Rectangle with width and height.
Args:
width (float): The width of the rectangle.
height (float): The height of the rectangle. 
"""
        self.width = width
        self.height = height

    def area(self):
"""
Calculate the area of the rectangle.
Returns:
float: Area of the rectangle.
"""
        return self.width * self.height

    def perimeter(self):
"""
Calculate the perimeter of the rectangle.
Returns:
float: Perimeter of the rectangle.
"""
        return 2 * (self.width + self.height)


def shape_info(shape):
"""
Print the area and perimeter of a shape using duck typing.
Args:
shape (object): Any object with area and perimeter methods.
"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

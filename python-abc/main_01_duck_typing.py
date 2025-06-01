#!/usr/bin/python3
"""
This script demonstrates polymorphism with abstract shapes
by creating instances of Circle and Rectangle and using shape_info.
"""

from task_01_duck_typing import Circle, Rectangle, shape_info

if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)

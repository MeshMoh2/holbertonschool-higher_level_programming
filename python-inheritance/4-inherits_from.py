#!/usr/bin/python3
"""
This module provides a function to check if an object
is an instance of a subclass (not the class itself) of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance against.

    Returns:
        True if obj is an instance of a subclass of a_class,
        but not a direct instance of a_class itself. Otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

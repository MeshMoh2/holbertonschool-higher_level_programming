#!/usr/bin/python3
"""
This module defines a function that checks if
an object is exactly an instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class

#!/usr/bin/python3
"""
This module provides a function to determine if an object
is an instance of, or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or inherits from it.

    Args:
        obj: Any object.
        a_class: A class to check against.

    Returns:
        True if obj is an instance of a_class or a subclass,
        otherwise False.
    """
    return isinstance(obj, a_class)

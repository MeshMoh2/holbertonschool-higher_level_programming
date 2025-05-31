#!/usr/bin/python3
"""
This module contains the function lookup which returns
a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing names of attributes and methods of the object.
    """
    return dir(obj)

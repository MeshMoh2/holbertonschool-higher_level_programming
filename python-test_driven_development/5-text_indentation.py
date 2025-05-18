#!/usr/bin/python3
"""
This module defines a function that prints text with two new lines after
each '.', '?', or ':' character.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', or ':' character.

    Args:
        text (str): The input string to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".:?":
            print(buffer.strip())
            print()
            buffer = ""
    if buffer.strip():
        print(buffer.strip())

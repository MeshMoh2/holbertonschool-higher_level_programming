#!/usr/bin/python3
"""
This module defines a function that prints text with two new lines after
each '.', '?' or ':' character.
"""
import sys


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', or ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for i, char in enumerate(text):
        buffer += char
        if char in ".:?":
            sys.stdout.write(buffer.strip() + "\n\n")
            buffer = ""

    if buffer.strip():
        sys.stdout.write(buffer.strip())

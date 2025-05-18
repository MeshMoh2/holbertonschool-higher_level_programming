#!/usr/bin/python3
"""
This module defines a function that prints text with two new lines after
each '.', '?' or ':' character.
"""


def text_indentation(text):
    """
    Prints a formatted version of text with 2 new lines after '.', '?', or ':'.

    Args:
        text (str): The input string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for i, char in enumerate(text):
        if char in ".:?":
            print(text[start:i + 1].strip())
            print()
            start = i + 1
            while start < len(text) and text[start] == " ":
                start += 1
    if start < len(text):
        print(text[start:].strip(), end="")

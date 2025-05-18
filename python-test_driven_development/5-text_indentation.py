#!/usr/bin/python3
"""
This module defines a function that prints text with two new lines after
each '.', '?' or ':' character.
"""


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

    i = 0
    length = len(text)
    while i < length:
        char = text[i]
        print(char, end="")
        if char in ".:?":
            print("\n")
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1

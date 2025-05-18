#!/usr/bin/python3
"""
This module defines a function that prints text with two new lines after
each '.', '?' or ':' character.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', or ':' character.

    Args:
        text (str): The input string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentence = ""
    for char in text:
        sentence += char
        if char in ".:?":
            print(sentence.strip())
            print()
            sentence = ""
    if sentence.strip():
        print(sentence.strip(), end="")

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

    new_text = ""
    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in ".:?":
            new_text = new_text.strip() + "\n\n"
            print(new_text, end="")
            new_text = ""
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    if new_text.strip():
        print(new_text.strip(), end="")

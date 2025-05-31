#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends the built-in list
with print notifications on modifications.
"""


class VerboseList(list):
    """
    A custom list class that prints messages when items are added or removed.
    """

    def append(self, item):
        """
        Append an item to the list and print a message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with elements from the iterable and print a message.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Print a message and remove the first occurrence of item from the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop and return the item at index (default last), and print a message.
        """
        item = self[index]  # retrieve before popping to include in message
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

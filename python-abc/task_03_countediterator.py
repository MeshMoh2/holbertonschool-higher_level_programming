#!/usr/bin/env python3
"""
This module defines a CountedIterator class that wraps an iterator
and counts how many items have been iterated.
"""


class CountedIterator:
    """
    An iterator that counts how many items have been returned.
    """

    def __init__(self, iterable):
        """
        Initialize the counted iterator.

        Args:
            iterable: Any iterable object.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.

        Returns:
            The next item in the iterator.

        Raises:
            StopIteration: When there are no more items.
        """
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated.

        Returns:
            int: The count of iterated items.
        """
        return self.count

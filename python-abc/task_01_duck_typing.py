#!/usr/bin/env python3
"""VerboseList: Custom list with notifications on mutation methods."""


class VerboseList(list):
    """Custom list subclass that prints messages on changes."""

    def append(self, item):
        """Append item to the list and print notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list with items from iterable and print notification."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item from the list and print notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from the list at index and print notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

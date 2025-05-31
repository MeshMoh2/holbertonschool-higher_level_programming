#!/usr/bin/env python3
"""VerboseList: Custom list subclass with notifications on changes."""


class VerboseList(list):
    """List subclass that prints messages when modified."""

    def append(self, item):
        """Append item and print notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print how many items were added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item and print notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item at index and print notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

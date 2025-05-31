#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList is a subclass of list that has
    a method to print the list in sorted order.

    Example:
        >>> m = MyList()
        >>> m.append(3)
        >>> m.append(1)
        >>> m.append(2)
        >>> m.print_sorted()
        [1, 2, 3]
        >>> print(m)
        [3, 1, 2]

        >>> m = MyList()
        >>> m.append(-2)
        >>> m.append(-5)
        >>> m.append(0)
        >>> m.print_sorted()
        [-5, -2, 0]
        >>> print(m)
        [-2, -5, 0]

        >>> empty = MyList()
        >>> empty.print_sorted()
        []
        >>> print(empty)
        []
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        The original list is not modified.
        """
        print(sorted(self))

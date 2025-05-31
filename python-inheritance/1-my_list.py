#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList is a subclass of list that has
    a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        The original list is not modified.
        """
        print(sorted(self))

#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList is a subclass of list with an added method
    to print the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        without modifying the original list.
        """
        print(sorted(self))

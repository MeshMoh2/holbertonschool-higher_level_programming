#!/usr/bin/env python3
"""
This module demonstrates the use of mixins to create
a Dragon class that can both swim and fly.
"""


class SwimMixin:
    """
    Mixin class that adds swimming ability.
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that adds flying ability.
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon that can swim and fly by using mixins.
    """

    def roar(self):
        print("The dragon roars!")

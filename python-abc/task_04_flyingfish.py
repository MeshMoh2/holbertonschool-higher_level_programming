#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance with a FlyingFish class
inheriting from both Fish and Bird.
"""


class Fish:
    """
    Represents a fish with basic behaviors.
    """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Represents a bird with basic behaviors.
    """

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A FlyingFish inherits from both Fish and Bird.
    Overrides swim, fly, and habitat methods.
    """

    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

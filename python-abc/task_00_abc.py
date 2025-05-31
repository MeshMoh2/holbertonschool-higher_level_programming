#!/usr/bin/env python3
"""
This module defines an abstract Animal class and two concrete subclasses:
Dog and Cat, each implementing their own sound.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an Animal.
    All subclasses must implement the sound() method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by any subclass.
        Should return the sound the animal makes.
        """
        pass


class Dog(Animal):
    """
    A Dog class that inherits from Animal and implements the sound method.
    """

    def sound(self):
        """
        Return the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    A Cat class that inherits from Animal and implements the sound method.
    """

    def sound(self):
        """
        Return the sound a cat makes.
        """
        return "Meow"

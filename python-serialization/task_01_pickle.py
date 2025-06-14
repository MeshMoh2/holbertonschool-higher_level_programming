#!/usr/bin/python3
"""Module for pickling and unpickling a custom Python object."""

import pickle


class CustomObject:
    """A custom class with attributes and serialization methods."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file.

        Args:
            filename (str): The name of the file to write the object to.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass  # Fail silently as instructed

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file.

        Args:
            filename (str): The file to load the object from.

        Returns:
            CustomObject or None: The deserialized object or None on failure.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
        return None

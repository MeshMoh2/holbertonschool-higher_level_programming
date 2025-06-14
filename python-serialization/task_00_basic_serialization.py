#!/usr/bin/python3
"""Module for basic JSON serialization and deserialization."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save to a file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The filename to save the JSON data to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize to a Python dictionary.

    Args:
        filename (str): The filename of the JSON file to read.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

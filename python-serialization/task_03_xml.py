#!/usr/bin/python3
"""Module to serialize and deserialize Python dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The file to write the XML data to.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    try:
        with open(filename, 'wb') as xml_file:
            tree.write(xml_file, encoding='utf-8', xml_declaration=True)
    except Exception:
        pass  # Silently fail as not specified otherwise


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The XML file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except Exception:
        return {}

#!/usr/bin/python3
"""inilialise le code"""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """define la fonction"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Failed to write XML to {filename}: {e}")

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except Exception as e:
        print(f"Failed to read or parse XML from {filename}: {e}")
        return {}

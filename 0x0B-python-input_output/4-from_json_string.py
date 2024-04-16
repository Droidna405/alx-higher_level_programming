#!/usr/bin/python3
"""JSON str representation into a Python obj"""


def from_json_string(my_str):
    """
    Convert a JSON string representation into a Python object (data structure).

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    import json

    return json.loads(my_str)

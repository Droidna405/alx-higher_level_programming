#!/usr/bin/python3

import json
"""Returns the JSON rep of an obj (strng)."""


def to_json_string(my_obj):
    """
    Args:
        my_obj: the obj to be converted to JSON
    Returns:
        str: the JSON rep of the obj
    """
    return json.dumps(my_obj, sort_keys=True)

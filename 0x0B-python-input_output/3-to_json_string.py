#!/usr/bin/python3
"""Returns the JSON rep of an obj (strng)."""


def to_json_string(my_obj):
    """
    Args:
        my_obj: the obj to be converted to JSON
    Returns:
        str: the JSON rep of the obj
    """
    if isinstance(my_obj, (int, float, bool, str, type(None))):
        return str(my_obj)
    elif isinstance(my_obj, list):
        return '[' + ', '.join(to_json_string(elem) for elem in my_obj) + ']'
    elif isinstance(my_obj, dict):
        return '{' + ', '.join(
            f'"{key}": {to_json_string(value)}'
            for key, value in my_obj.items()
        ) + '}'
    else:
        raise TypeError(f'{type(my_obj)} is not JSON serializable')

#!/usr/bin/python3

"""Module to define a function for checking object class inheritance."""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if it inherits from, 
    a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or 
    its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
        

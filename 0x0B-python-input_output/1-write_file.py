#!/usr/bin/python3
"""Python function that writes a string to a text file."""


def write_file(filename="", text=""):
    """
    Args:
        filename (strng): the name of the text file to write to.
        text (strng): the string to write to the file
    Returns:
        int: the number of chars writen in the file.
    """

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)

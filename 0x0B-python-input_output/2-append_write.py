#!/usr/bin/python3
"""Appends a string at the end of a txt file (UTF8)"""


def append_write(filename="", text=""):
    """
    Args:
        filename (strng): The name of the text file.
        text (strng): The string to append to the file.
    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)

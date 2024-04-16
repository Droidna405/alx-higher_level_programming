#!/usr/bin/python3
"""Reads a txt file(UTF8) and prints it to stdout."""


def read_file(filename=""):
    """
    Args:
        filename (strng): The name of the txt file to read.
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')


if __name__ == "__main__":
    read_file

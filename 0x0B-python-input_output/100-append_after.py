#!/usr/bin/python3
"""Inserts a line of tst into a file after each line"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert.

    Returns:
        None

    Raises:
        None
    """

    # Open the file for reading and writing
    with open(filename, 'r+') as file:
        # Read all lines into a list
        lines = file.readlines()
        file.seek(0)  # Move the file pointer to the beginning

        # Iterate over each line in the list
        for line in lines:
            # Write the original line to the file
            file.write(line)
            # If the search string is found in the line, append the new string
            if search_string in line:
                file.write(new_string)


        file.truncate()

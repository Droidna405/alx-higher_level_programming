#!/usr/bin/python3
"""Write an obj to a txt file in JSON format"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file in JSON format.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write to.

    Returns:
        None

    """
    import json

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
                            

#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the characters to look for
    special_chars = ['.', '?', ':']

    # Initialize an empty string to store the formatted text
    formatted_text = ""

    # Iterate through each character in the text
    for char in text:
        # Add the character to the formatted text
        formatted_text += char

        # If the character is a special character, add 2 new lines
        if char in special_chars:
            formatted_text += '\n\n'

    # Print the formatted text
    print(formatted_text.strip())

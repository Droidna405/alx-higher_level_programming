#!/usr/bin/python3
"""1-my_list.py

This module defines a MyList class that inherits from the built-in list class
and provides a method to print the list sorted in ascending order.
"""


class MyList(list):
    """
    MyList inherits from the built-in list class and adds a method to print
    the list sorted in ascending order.

    Raises:
        TypeError: If the element added to the list is not of type int.
    """

    def __init__(self):
        """
        Initialize a new MyList instance.
        """
        super().__init__()

    def append(self, value):
        """
        Appends a value to the list.

        Args:
            value: The value to append. Must be of type int.

        Raises:
            TypeError: If the value is not of type int.
        """
        if not isinstance(value, int):
            raise TypeError("only integer elements are allowed")
        super().append(value)

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.

        This method does not modify the original list.
        """
        print(sorted(self))  # Create a sorted copy and print it

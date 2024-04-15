#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """
    MyList class inherits from list and provides additional functionality.

    Public Methods:
        print_sorted(self): Prints the list in sorted order (ascending).

    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).

        """
        sorted_list = sorted(self)
        print(sorted_list)

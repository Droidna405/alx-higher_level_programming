#!/usr/bin/python3
"""
This module defines a Square class.

The Square class represents a square shape with a size attribute.
It provides methods to set and retrieve the size, calculate the area,
and print a square pattern using '#' characters.

Example:
    my_square = Square(3)
    my_square.my_print()

    # Output:
    ###
    ###
    ###

    my_square.size = 10
    my_square.my_print()

    # Output:
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########

    my_square.size = 0
    my_square.my_print()

    # Output:
    (Empty line)

Classes:
    Square: Represents a square shape.

"""


class Square:
    """
    Represents a square shape.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")

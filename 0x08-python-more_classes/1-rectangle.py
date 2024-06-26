#!/usr/bin/python3

"""
This module defines a Rectangle class representing a geometric rectangle.
"""


class Rectangle:
    """
    Rectangle class represents a geometric rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object with optional
        width and height.
        Args:
            width (int): The width of the
            rectangle (default is 0).
            height (int): The height of the
            rectangle (default is 0).
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of
        the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.
        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
                ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

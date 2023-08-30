#!/usr/bin/python3
# 5-square.py

"""My Square Class"""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        for idx in range(0, self.__size):
            [print("#", end="") for row in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

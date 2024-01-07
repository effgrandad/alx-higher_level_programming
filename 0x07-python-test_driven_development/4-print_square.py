#!/usr/bin/python3
"""Module to print_square method."""


def print_square(size):
    """Method to print square with # characters.

    Args:
        size (int): The  square's side.

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range (size):
        [print("#", end="") for j in range(size)]
        print("")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")


#!/usr/bin/python3
"""
Module to add two integer method
"""


def add_integer(a, b=98):
    """Return the integer sum of a and b.
    Args:
        a: first int.
        b: second int, default 98.

    Raises:
        TypeError: If either of a or b are not integer, float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main___":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

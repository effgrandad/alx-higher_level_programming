#!/usr/bin/python3
"""Module for inherits_from method"""


def inherits_from(obj, a_class):
    """Verify whether an object precisely reflects a particular class instance

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

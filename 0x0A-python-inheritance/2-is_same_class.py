#!/usr/bin/python3
"""Module for is_same_class method"""


def is_same_class(obj, a_class):
    """Verify whether an object precisely reflects a particular class instance

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

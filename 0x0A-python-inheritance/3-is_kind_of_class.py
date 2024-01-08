#!/usr/bin/python3
"""Module for is_kind_of_class method."""


def is_kind_of_class(obj, a_class):
    """Verify whether an object precisely reflects a particular class instance

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False

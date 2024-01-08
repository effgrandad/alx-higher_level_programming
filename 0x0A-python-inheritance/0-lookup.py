#!/usr/bin/python3
"""Module for lookup function"""

def lookup(obj):
    """Looks up for object attributes and methods
    Args:
        obj(object): object to the list.

        Returns:
            list: list of the attributes.
    """
    return dir(obj)

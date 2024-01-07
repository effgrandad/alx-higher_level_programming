#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """A function to locate the largest integer in a list of integers and return it
        Returning None, the function checks if the list is empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

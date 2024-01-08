#!/usr/bin/python3
"""Module of MyList class"""


class MyList(list):
    """Sorted printing is implemented for the built-in list class"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

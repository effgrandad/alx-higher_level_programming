#!/usr/bin/python3
"""Define a append_write function"""

def append_write(filename="", text=""):
    """Appends the string to the end of a UTF8 text file

    Args:
        filename (str): name of the file to append
        text (str): string to append to a file
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", enconding="utf-8") as f:
        return f.write(text)

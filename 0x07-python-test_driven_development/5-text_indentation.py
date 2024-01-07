#!/usr/bin/python3
"""Module for text-indentation method"""


def text_indentation(text):
    """Method of summing up 2 new line after '.?:' chars.

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    h = 0
    while h < len(text) and text[h] == ' ':
        h += 1

    while h < len(text):
        print(text[h], end="")
        if text[h] == "\n" or text[h] in ".?:":
            if text[h] in ".?:":
                print("\n")
            h += 1
            while h < len(text) and text[h] == ' ':
                h += 1
            continue
        h += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

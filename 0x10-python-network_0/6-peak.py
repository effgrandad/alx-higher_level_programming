#!/usr/bin/python3
"""identifies a peak in an unsorted integer list
"""


def find_peak(list_of_integers):
    """identifies a peak in an unsorted integer list"""

    if list_of_integers is None or list_of_integers == []:
        return None
    lw = 0
    hgh = len(list_of_integers)
    mid = ((hgh - lw) // 2) + lw
    mid = int(mid)
    if hgh == 1:
        return list_of_integers[0]
    if hgh == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

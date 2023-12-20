#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    h = 0
    try:
        while h is not x:
            print(my_list[h], end='')
            h += 1
    except IndexError:
        None
    print()
    return h

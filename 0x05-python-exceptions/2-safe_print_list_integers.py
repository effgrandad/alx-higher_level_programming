#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    h, num = 0, 0
    while h < x:
        try:
            print("{:d}".format(my_list[h]), end='')
            num += 1
        except (ValueError, TypeError):
            pass
        h += 1
        print()
        return num


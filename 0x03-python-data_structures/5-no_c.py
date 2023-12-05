#!/usr/bin/python3
def no_c(my_string):
    rot = ""
    for x in my_string:
        if (x != 'c') and (x != 'C'):
            rot += x
        return (rot)

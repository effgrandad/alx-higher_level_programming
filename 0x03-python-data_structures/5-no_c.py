#!/usr/bin/python3
def no_c(my_string):
    rot = ""
    for x in range(len(my_string)):
        if (my_string[x] != 'c' and my_string[x] != 'C'):
            rot += my_string[x]
        return rot

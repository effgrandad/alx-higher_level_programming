#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b_list = my_list[:]
    for count, x in enumerate(my_list):
        if x % 2 == 0:
            b_list[count] = True
        else:
            b_list[count] = False
    return (b_list)

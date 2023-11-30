#!/usr/bin/python3
def print_last_digit(value):
    if value < 0:
        last_num = (-value % 10)
    elif value >= 0:
        last_num = value % 10
    print("{:d}".format(last_num), end="")
    return last_num


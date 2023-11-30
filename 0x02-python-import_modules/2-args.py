#!/usr/bin/python3
#  Prints the total number of arguments and its list
if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for k in range(1, size + 1):
            print("{}: {}".format(k, arg[k]))

    elif size == 0:
        print("{} arguments.".format(size))

    else:
        print("{} argument:".format(size))
        print("{}: {}".format(size, arg[1]))


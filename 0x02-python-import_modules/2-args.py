#!/bin/pythn3
if __name__ == '__main__':
    import sys

    num = len(sys.argv) - 1
    if num == 0:
        print("0 arguments:")
    elif num == 1:
        print("1 argumnt:")
    else:
        print("{} arguments:".forma(num))
    for j in range(num):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))

#!/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    e = 10
    f = 5
    print("{} + {} = {}".format(e, f, add(e, f)))
    print("{} - {} = {}".format(e, f, sub(e, f)))
    print("{} * {} = {}".format(e, f, mul(e, f)))
    print("{} / {} = {}".format(e, f, div(e, f)))

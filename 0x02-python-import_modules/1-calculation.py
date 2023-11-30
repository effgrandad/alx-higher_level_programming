#!/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    b = 10
    d = 5
    print("{} + {} = {}".format(b, d, add(b, d)))
    print("{} - {} = {}".format(b, d, sub(b, d)))
    print("{} * {} = {}".format(b, d, mul(b, d)))
    print("{} / {} = {}".format(b, d, div(b, d)))

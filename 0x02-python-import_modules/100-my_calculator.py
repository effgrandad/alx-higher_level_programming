#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    b = int(sys.argv[1])
    d = int(sys.argv[3])
    op = sys.argv[2]
    if op == "+":
        print("{} + {} = {}".format(b, d, add(b, d)))
    elif op == "-":
        print("{} - {} = {}".format(b, d, sub(b, d)))
    elif op == "*":
        print("{} * {} = {}".format(b, d, mul(b, d)))
    elif op == "/":
        print("{} / {} = {}".format(b, d, div(b, d)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

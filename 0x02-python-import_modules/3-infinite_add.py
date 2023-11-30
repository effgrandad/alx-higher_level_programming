#!/usr/bin/python3
def add_arg(argv):
    h = len(argv) - 1
    if h == 0:
        print("{:d}".format(h))
        return
    else:
        m = 1
        add = 0
        while m <= h:
            add += int(argv[m])
            m += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)



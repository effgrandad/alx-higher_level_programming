#!/usr/bin/python3
for m in range(ord('z'), ord('a') - 1, -2):
    print("{}{}".format(chr(m), chr(1 - 33)), end='')

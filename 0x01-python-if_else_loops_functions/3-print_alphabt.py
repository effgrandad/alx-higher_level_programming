#!/usr/bin/python3
for h in range(97, 123):
    if h in [101, 113]:
        continue
    print("{}".format(chr(h)), end='')

#!/usr/bin/python3
def magic_calculation(b, d):
    from magic_calculation_102 import add, sub
    if b < d:
        e = add(b, d)
        for i in range(4, 6):
            e = add(e, i)
        return e
    else:
        return (sub(b, d))
    return ()

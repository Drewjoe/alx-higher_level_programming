#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    m = ()
    for n in (tuple_a, tuple_b):
        if len(n) == 0:
            n = (0, 0)
        elif len(n) == 1:
            n = (n[0], 0)
        if m == ():
            m = n
    return n[0] + m[0], n[1] + m[1]

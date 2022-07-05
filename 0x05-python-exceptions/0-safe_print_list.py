#!/usr/bin/python3
""" Prints x elements of a list.

Args: my_list
Returns: the real number of elements printed

Note: x represents the number of elements to print
    x can be bigger than the length of my_list
"""


def safe_print_list(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            n += 1
        except IndexError:
            break
    print()
    return n

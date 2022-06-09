#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = a_dictionary.copy()
    for x, y in tmp.items():
        if value == y:
            a_dictionary.pop(x)
    return a_dictionary

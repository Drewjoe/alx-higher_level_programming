#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ''
    if n > len(str) or n < 0:
        return str
    for t in str:
        if t != str[n]:
            new_str += t
    return new_str

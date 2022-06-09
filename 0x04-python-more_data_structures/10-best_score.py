#!/usr/bin/python3
def best_score(a_dictionary):
    m = 0
    res = ""
    if a_dictionary:
        for s, t in a_dictionary.items():
            if t > m:
                res = s
                m = t
        return res
    else:
        return None

#!/usr/bin/python3
for t in range(ord("a"), ord("z") + 1):
    if chr(t) != 'q' and chr(t) != 'e':
        print("{:c}".format(t), end="")

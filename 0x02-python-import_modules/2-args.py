#!/usr/bin/python3
import sys


def main(*argv):
    i = 0
    s = len(sys.argv) - 1
    if s == 1:
        print(f"{s:d} argument:")
    elif s == 0:
        print(f"{s:d} arguments.")
    else:
        print(f"{s:d} arguments:")
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    main()

#!/usr/bin/python3
import hidden_4


def main():
    s = dir(hidden_4)
    for i in range(len(s)):
        if(s[i][0] != '_'):
            print("{}".format(s[i]))


if __name__ == "__main__":
    main()

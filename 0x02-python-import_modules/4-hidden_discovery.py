#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    s = dir(hidden_4)
    for i in range(len(s)):
        if(s[i][0] != '__'):
            print(f"{s[i]}")

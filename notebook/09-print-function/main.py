#!/usr/bin/env python3

#
# file: main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
import sys


def main():
    n = int(input())
    s = str()

    for it in range(n):
        s += str(it + 1)

    print(s)


if __name__ == '__main__':
    sys.exit(main())

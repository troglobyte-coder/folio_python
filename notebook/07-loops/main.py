#!/usr/bin/env python3

#
# file: main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
import sys


def main():
    n = int(input())

    for it in range(n):
        print(it * it)


if __name__ == '__main__':
    sys.exit(main())

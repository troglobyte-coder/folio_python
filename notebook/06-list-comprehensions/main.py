#!/usr/bin/env python3

#
# file: main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
import sys


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    answers = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(answers)


if __name__ == '__main__':
    sys.exit(main())

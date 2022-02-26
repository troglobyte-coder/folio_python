#!/usr/bin/env python3

#
# file: main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
import sys


def solveMeFirst(a,b):
    return a+b


def main():
    num1 = int(input())
    num2 = int(input())
    res = solveMeFirst(num1,num2)
    print(res)


if __name__ == '__main__':
    sys.exit(main())

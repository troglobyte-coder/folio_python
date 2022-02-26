#!/usr/bin/env python3

#
# file: main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
import sys


def is_leap(year):
    leap = False

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True

    return leap


def main():
   year = int(input())
   print(is_leap(year))

if __name__ == '__main__':
    sys.exit(main())

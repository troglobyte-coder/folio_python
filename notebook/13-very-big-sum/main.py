#!/usr/bin/env python3

#
# file: main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
import sys
import os


def aVeryBigSum(ar):
    count = 0
    for i in ar:
        count += i
    return count


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

if __name__ == '__main__':
    sys.exit(main())

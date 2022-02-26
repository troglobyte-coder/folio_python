#!/usr/bin/env python3

#
# file: main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
import sys
import math
import os
import random
import re


def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    col = 0
    
    for row in range(len(arr)):
        sum1 += arr[row][col]
        col + 1

    col = len(arr) - 1
    for row in range(col):
        sum2 += arr[row][col]
        col - 1

    diff = sum1 - sum2
    if diff < 0:
        diff = (diff - 0)
        return diff
    else:
        return diff


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')

    fptr.close()


if __name__ == '__main__':
    sys.exit(main())
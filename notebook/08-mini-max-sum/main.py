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


def miniMaxSum(arr):
    sum_value = 0
    min_value = 0
    max_value = 0
    num_value = 0

    for i in range(len(arr)):
        num_value = arr[i]
        sum_value += num_value

        if (i == 0):
            max_value = num_value
            min_value = num_value
        else:
            if (num_value > max_value):
                max_value = num_value
            elif (num_value < min_value):
                min_value = num_value

    print(f'{sum_value - max_value} {sum_value - min_value}')


def main():
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


if __name__ == '__main__':
    sys.exit(main())

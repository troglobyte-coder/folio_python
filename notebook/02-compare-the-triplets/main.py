#!/usr/bin/env python3

#
# file: main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
import sys
import os


def compareTriplets(a, b):
    count_alice = 0
    count_bob = 0

    for i in range(3):
        if a[i] > b[i]:
            count_alice += 1
        elif a[i] < b[i]:
            count_bob += 1

    return [count_alice, count_bob]


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


if __name__ == '__main__':
    sys.exit(main())

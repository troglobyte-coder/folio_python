#!/usr/bin/env python3

#
# file: main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
import math
import os
import random
import re
import sys


def main():
    n = int(input().strip())
    
    if n % 2 == 1 or 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')


if __name__ == '__main__':
    sys.exit(main())

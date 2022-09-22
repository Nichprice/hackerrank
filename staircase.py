#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    hash = "#"
    space = " "
    for step in range(1, n + 1):
        num_of_spaces = n - step
        num_of_hash = step
        spaces = (num_of_spaces * space)
        hashes = (num_of_hash * hash)
        print(f"{spaces}{hashes}")
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    tot = sum(arr)
    miniMax = []
    for n in arr:
        miniMax.append(tot - n)
    big = max(miniMax)
    lit = min(miniMax)
    answer = [lit, big]
    print(*answer)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

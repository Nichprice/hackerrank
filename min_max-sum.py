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
sums = []
def miniMaxSum(arr):
    # Write your code here
    for n in range(0, 5):
        sums.append(sum(arr) - arr[n])
    min_max = [min(sums), max(sums)]
    print(*min_max)        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

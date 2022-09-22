#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s = start house
#  2. INTEGER t = end house
#  3. INTEGER a = apple tree spot
#  4. INTEGER b = orange tree spot
#  5. INTEGER_ARRAY apples = distance from apple tree
#  6. INTEGER_ARRAY oranges = distance from orange tree
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    new_app = []
    app_total = 0
    for apple in apples:
        new_app.append(a + apple)
    for appspot in new_app:
        if s <= appspot <= t:
            app_total += 1
    new_or = []
    or_total = 0
    for orange in oranges:
        new_or.append(b + orange)
    for orspot in new_or:
        if s <= orspot <= t:
            or_total += 1
    print(app_total)
    print(or_total)
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

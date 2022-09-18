#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
s = "07:05:45PM"

def timeConversion(s):
    # Write your code here
    split = s.split(":")
    switcher = split[2]
    if "PM" in split[2]:
      first = int(split[0]) +12
      split[0] = str(first)
    broken_decider = list(switcher)
    print(broken_decider)
    prbroken_decider.pop()
  
timeConversion(s)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()

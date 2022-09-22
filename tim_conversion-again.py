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

def timeConversion(s):
    # Write your code here
    arr = list(s.split(":"))
    lead_num = arr[0]
    if arr[2][2:] == "PM":
        if lead_num != "12":
            arr[0] = str(int(lead_num) + 12)
    else:
        if lead_num == "12":
            arr[0] = str("00")
    arr[2] = arr[2][:2]
    mt = str(":".join(arr))
    return mt

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

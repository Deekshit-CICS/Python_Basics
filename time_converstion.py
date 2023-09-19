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
# input: 12:40:22AM         => no space betweeen time and AM/PM
# output: 00:40:22 

def timeConversion(s):
    # Write your code here
    if ("AM" in s):
        if "12" in s[0:2]:
            s = '00:'+s[3:8]
        else:
            s = s[0:8]
        s.strip()
    if "PM" in s:
        if s[0:2] in "12":
            s = s[:-2]
        else:
            s = str(12+int(s[0:2]))+':'+s[3:8]
        s.strip()
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pnum = 0
    nnum = 0
    znum = 0
    for i in arr:
        if (i > 0):
            pnum = pnum + 1
        elif (i < 0):
            nnum =nnum + 1
        else:
            znum = znum + 1
    
    print(format((pnum/n),"6f"))
    print(format((nnum/n),"6f"))
    print(format((znum/n),"6f"))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

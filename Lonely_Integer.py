#!/bin/python3

import math
import os
import random
import re
import sys

# Sample Input    
#  3
# 1 1 2
# Expected output:
# 2


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def count(lst, x):
    count= 0
    for ele in lst:
        if (x == ele):
            count = count+1
    return count

def lonelyinteger(a):
    # Write your code here
    print(a)
    count_dict = {}
    for i in a:
        count_dict[i] = count(a,i)
    print(count_dict)
    for i in count_dict:
        if(count_dict[i] > 2):
            pass
        else:
            return count_dict[i] 
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()


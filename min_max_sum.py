#!/bin/python3

#  I/O  1 2 3 4 5
import math
import os
import random
import re
import sys
import itertools as it

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    list1 = []
    # Write your code here
    
    unique_combinations = list(it.combinations(arr,4))
    # print(unique_combinations[0])
    
    for i in range(len(unique_combinations)):
        list1.append(sum(unique_combinations[i]))

    print(min(list1),max(list1))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

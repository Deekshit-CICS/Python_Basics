#!/bin/python3

import math
import os
import random
import re
import sys
 
# Sample Input
# 07:05:45PM
# Sample Output
# 19:05:45
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code hear
    print(s)
    s1 = s.split(":")
    print(s1)
    # time1 = str(s1[0]+1),":",str(s1[1]),":"
    hrs = s1[0]
    mins = str(s1[1]).strip()
    sec= s1[2][:2].strip()
    mn = s1[2][2:4].strip()
    print(mn)
    if ((hrs == "12") and (mn == "AM")):
        hrs = "00"
    elif ((hrs == "12") and (mn == "PM")):
        pass
    elif(mn == "PM"):
        hrs = str(int(s1[0])+12).strip()
    print(hrs,":",mins,":",sec)
    final_time = hrs,":",mins,":",sec
    # str_time =''
    # for item in final_time:
    #     str_time = str_time + item
    # print(str_time)
    
    str_time = ''.join(final_time)
    return str_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()

    
    
   

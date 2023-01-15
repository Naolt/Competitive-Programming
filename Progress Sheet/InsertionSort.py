#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    if(not(n <= 1000 and n >= 1)):
        return
    for x in arr:
        if(not( x >= -10000 and x <= 10000 )):
            return
        
    current = arr[-1]
    index = n-2
    while (current < arr[index]) and (index >= 0):
        arr[index+1] = arr[index]
        print(*arr)
        index -= 1
    arr[index+1] = current
    print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

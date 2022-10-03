#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    if(not(len(a) <= 600 and len(a) >= 2)):
        return
    for x in a:
        if(not(x >= 1 and x <= 2*(10**6))):
            return

        
    swaps = 0
    for x in range(len(a)-1):
        for y in range(len(a)-1):
            if(a[y]>a[y+1]):
                temp = a[y]
                a[y] = a[y+1]
                a[y+1] = temp
                swaps += 1
    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a)-1]))
        
            
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

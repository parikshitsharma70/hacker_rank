#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    l = len(arr)
    temparr = sorted(arr)
    temparr1 = temparr[0:l-1]
    temparr2 = temparr[1:]
    
    print(str(sum(temparr1)) + " "+ str(sum(temparr2)))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    day_night = s[-2:]
    time = int(s[0:2])
    output = ""
    
    if day_night == "AM":
        if time == 12:
            output = "00"+s[2:-2]
        else:
            output = s[:-2]
    elif day_night == "PM":
        if time == 12:
            output = "12"+s[2:-2]
        else:
            output = str(time+12)+s[2:-2]
            
    return output
            

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

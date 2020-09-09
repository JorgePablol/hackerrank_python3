# CAPITALIZE!
# LINK = https://www.hackerrank.com/challenges/capitalize/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split(" ")

    s1 = [i.capitalize() for i in s]
    s1 = " ".join(s1)
    return s1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()    
    

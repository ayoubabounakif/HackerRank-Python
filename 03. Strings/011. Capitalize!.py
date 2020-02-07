# Problem: https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    list_ = s.split(" ")
    list_ = [i.capitalize() for i in list_]
    return ' '.join(list_)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

"""
s = input()
for x in s[:].split():
    s = x.capitalize()
    print (s[:], end=' ')

"""








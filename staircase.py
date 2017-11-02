# PROBLEM: https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import sys


n = int(input().strip())
for i in range(1,n+1):
    ln = ""
    for j in reversed(range(n)):
        if j-i >= 0:
            ln += " "
        else:
            ln += "#"
    print(ln)

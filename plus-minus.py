# PROBLEM: https://www.hackerrank.com/challenges/plus-minus/problem
#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos = neg = zero = 0
for number in arr:
    if number > 0:
        pos += 1
    elif number < 0:
        neg += 1
    else:
        zero += 1
print("{0:0.6f}".format(pos/len(arr)))
print("{0:0.6f}".format(neg/len(arr)))
print("{0:0.6f}".format(zero/len(arr)))

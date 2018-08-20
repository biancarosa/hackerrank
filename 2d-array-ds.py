# PROBLEM: https://www.hackerrank.com/challenges/2d-array
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = None
    for line in range(1,len(arr)-1):
        for column in range(1,len(arr)-1):
            current_hourglass_sum = arr[line-1][column-1] + arr[line-1][column] + arr[line-1][column+1] + arr[line][column] + arr[line+1][column-1] + arr[line+1][column] + arr[line+1][column+1]
            if max_sum is None or current_hourglass_sum > max_sum:
                max_sum = current_hourglass_sum
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

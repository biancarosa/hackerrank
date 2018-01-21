#!/bin/python3
# https://www.hackerrank.com/challenges/mini-max-sum/problem

import sys

def minMax(arr):
    # Complete this function
    s = sorted(arr)
    min = sum(s[0:-1])
    max = sum(s[1:])
    return (min, max)

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    min, max = minMax(arr)
    print(min, max)

#!/bin/python3
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
import sys

def birthdayCakeCandles(n, ar):
    d = {}
    m = 0
    for n in ar:
        if not d.get(n):
            d[n] = 0
        d[n] += 1
        if n > m:
            m = n
    return d[m]
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)

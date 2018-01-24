#!/bin/python3
# https://www.hackerrank.com/challenges/time-conversion/problem
import sys

def timeConversion(s):
    if s[8:] == 'PM':
        if s[0:2] != '12':
            converted = str(int(s[0:2]) + 12) + s[2:-2]
        else:
            converted = s[0:-2]  
    else:
        if s[0:2] != '12':
            converted = s[:-2]
        else:
            converted = '00' + s[2:-2]
    return converted

s = input().strip()
result = timeConversion(s)
print(result)

# PROBLEM: https://www.hackerrank.com/challenges/compare-the-triplets/problem
#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    bob, alice = (0, 0)
    if a0 > b0:
        alice += 1
    elif b0 > a0:
        bob += 1
    if a1 > b1:
        alice += 1
    elif b1 > a1:
        bob += 1
    if a2 > b2:
        alice += 1
    elif b2 > a2:
        bob += 1
    return (alice, bob) 

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))



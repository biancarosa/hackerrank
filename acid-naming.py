#!/bin/python3

# Acid Naming
# https://www.hackerrank.com/contests/w36/challenges/acid-naming

import sys

def acidNaming(acid_name):
    if acid_name[-2:] == 'ic':
        if acid_name[0:5] == 'hydro':
            return 'non-metal acid'
        return 'polyatomic acid'
    return 'not an acid'

if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)
        print(result)

# Revised Russian Roullete
# https://www.hackerrank.com/contests/w36/challenges/revised-russian-roulette/submissions/code/1305806039
# 
# #!/bin/python3

import sys

def revisedRussianRoulette(doors):
    min = []
    max = 0
    for i in range(len(doors)):
        if doors[i] == 1:
            max = max + 1
            if i-1 not in min:
                min.append(i)
    return (len(min),max)   

if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (" ".join(map(str, result)))


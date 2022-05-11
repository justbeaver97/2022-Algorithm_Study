"""
16198번 - https://www.acmicpc.net/problem/16198

에너지 모으기
"""

import sys
input = sys.stdin.readline

N = int(input())
W = list(map(int, input().split()))

def recursion(energy):
    global answer
    if len(W)==2:
        if energy > answer:
            answer = energy
        return 
    else:
        for i in range(1, len(W)-1):
            energy += W[i-1]*W[i+1]
            tmp = W[i]
            del W[i]
            recursion(energy)
            W.insert(i,tmp)
            energy -= W[i-1]*W[i+1]

answer = 0
recursion(0)
print(answer)
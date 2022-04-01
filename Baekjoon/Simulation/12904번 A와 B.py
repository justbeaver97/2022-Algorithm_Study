"""
12904번 - https://www.acmicpc.net/problem/12904

A와 B
"""

import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while (len(S) != len(T)):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]

print(1 if S == T else 0)
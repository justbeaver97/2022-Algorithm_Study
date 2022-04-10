"""
2439번 - https://www.acmicpc.net/problem/2439

별 찍기 2

reference
python sep - https://infinitt.tistory.com/11
"""

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N-1,-1,-1):
    print(" "*i,"*"*(N-i), sep="")
"""
2559번 - https://www.acmicpc.net/problem/2559

수열
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temperatures = list(map(int,input().split()))

range_temp = sum(temperatures[:K])
max_temp = range_temp
for i in range(K, N):
    range_temp += temperatures[i]
    range_temp -= temperatures[i-K]
    if range_temp > max_temp:
        max_temp = range_temp
print(max_temp)

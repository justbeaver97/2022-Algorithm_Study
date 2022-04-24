"""
1149번 - https://www.acmicpc.net/problem/10989

RGB 거리

오답이 나왔던 case
8
71 39 44
32 83 55
51 37 63
89 29 100
83 58 11
65 13 15
47 25 29
60 66 19
-> 253 (나는 310)
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
dp = [min(arr[0])] + [0]*(N-1)
dp_index = arr[0].index(min(arr[0]))

for i in range(1,N):
    arr[i][dp_index] = 1000
    dp[i] = min(arr[i])
    dp_index = arr[i].index(min(arr[i]))
print(sum(dp))
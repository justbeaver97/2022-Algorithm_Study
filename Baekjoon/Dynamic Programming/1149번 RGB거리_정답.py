"""
1149번 - https://www.acmicpc.net/problem/10989

RGB 거리
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))

for i in range(1,N):
    arr[i][0] += min(arr[i-1][1],arr[i-1][2])
    arr[i][1] += min(arr[i-1][0],arr[i-1][2])
    arr[i][2] += min(arr[i-1][0],arr[i-1][1])
print(min(arr[N-1]))
"""
10825번 - https://www.acmicpc.net/problem/10825

국영수
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(list(input().split()) for _ in range(N))
sorted_arr = sorted(arr, key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for score in sorted_arr:
    print(score[0])
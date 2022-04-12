"""
1546번 - https://www.acmicpc.net/problem/1546

평균
"""

import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

answer = 0
for score in scores:
    tmp = (score/max(scores)) * 100
    answer += tmp
print(answer/N)
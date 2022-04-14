"""
21921번 - https://www.acmicpc.net/problem/21921

블로그

오답 이유 - Runtime Error
sliding window 방식으로 풀지 않고, brute force하게 문제 해결
"""

import sys
input = sys.stdin.readline

X, N = map(int, input().split())
visitors = list(map(int, input().split()))
max_num, max_range = 0, 0

for i in range(X-N+1):
    tmp = 0
    for j in range(i,N+i):
        tmp += visitors[j]
    if tmp > max_num:
        max_num = tmp
        max_range = 1
    elif tmp == max_num and tmp != 0:
        max_range += 1
        
print(f"{max_num}\n{max_range}") if max_range != 0 else print("SAD")
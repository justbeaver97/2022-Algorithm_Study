"""
2531번 - https://www.acmicpc.net/problem/2531

회전 초밥
"""

import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = list(int(input()) for _ in range(N))
tmp = arr[:k-1]
arr = arr + tmp

max_length, diverse_sushi = 0, []
for i in range(N):
    tmp = arr[i:i+k]
    if len(set(tmp)) > max_length:
        max_length, diverse_sushi = len(set(tmp)), []
        diverse_sushi.append(tmp)
    elif len(set(tmp)) == max_length:
        diverse_sushi.append(tmp)

answer = 0
for sushi in diverse_sushi:
    if c in sushi:
        answer = len(set(sushi))
    elif c not in sushi:
        answer = len(set(sushi)) + 1
print(answer)
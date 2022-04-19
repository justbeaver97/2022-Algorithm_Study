"""
1654번 - https://www.acmicpc.net/problem/1654

랜선 자르기

못 풀었던 이유
start, end = 0, lengths[-1] -> 1, max(lengths)
print(mid) -> print(end)
"""

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lengths = list(int(input()) for _ in range(K))
start, end = 1, max(lengths)

while start <= end:
    mid, num_of_line = (start+end)//2, 0
    for length in lengths:
        num_of_line += length // mid
    
    if num_of_line >= N: start = mid + 1
    else:                end = mid - 1
print(end)

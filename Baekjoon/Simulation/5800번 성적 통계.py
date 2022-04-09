"""
5800번 - https://www.acmicpc.net/problem/5800

성적 통계
"""

import sys
input = sys.stdin.readline

K = int(input())
for i in range(K):
    tmp = list(map(int, input().split()))
    num, scores = tmp[0], sorted(tmp[1:])
    best, worst, gap = max(scores), min(scores), 0
    for j in range(0,len(scores)-1):
        if abs(scores[j]-scores[j+1]) > gap: gap = abs(scores[j]-scores[j+1])
    print(f"Class {i+1}")
    print(f"Max {best}, Min {worst}, Largest gap {gap}")
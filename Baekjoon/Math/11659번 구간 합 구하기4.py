"""
11659번 - https://www.acmicpc.net/problem/11659

구간 합 구하기 4
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

신기했던 점
import sys
input = sys.stdin.readline

안 쓰면 시간 초과, 쓰면 통과
"""

import sys
input = sys.stdin.readline

_, M = map(int, input().split())

arr = list(map(int, input().split()))
sum, tmp = [], 0
sum.append(0)

for item in arr:
    tmp += item
    sum.append(tmp)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j]-sum[i-1])
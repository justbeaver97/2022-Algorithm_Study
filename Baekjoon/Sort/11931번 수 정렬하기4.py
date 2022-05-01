"""
11931번 - https://www.acmicpc.net/problem/11931

수 정렬하기4
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(int(input()) for _ in range(N)), reverse=True)
print('\n'.join(map(str,arr)))
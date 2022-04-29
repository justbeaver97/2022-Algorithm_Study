"""
1427번 - https://www.acmicpc.net/problem/1427

소트인사이드
"""

import sys
input = sys.stdin.readline

N = sorted(list(input().rstrip()), reverse=True)
print(''.join(N))
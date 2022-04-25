"""
1181번 - https://www.acmicpc.net/problem/1181

단어 정렬
"""

import sys
input = sys.stdin.readline

N = int(input())
alphabets = list(set(input().rstrip('\n') for _ in range(N)))
for alphabet in sorted(alphabets, key = lambda x: (len(x), x)):
    print(alphabet)
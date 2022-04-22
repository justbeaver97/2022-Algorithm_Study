"""
15649번 - https://www.acmicpc.net/problem/15649

M과 N

reference
1. how to use permutation(especially M)
https://hjp845.tistory.com/158

2. how to use int list in permutation
https://programmers.co.kr/learn/courses/4008/lessons/12836
"""

import sys, itertools
input = sys.stdin.readline

N, M = map(int,input().split())
pool = list(range(1,N+1))
permute = list(map(' '.join, itertools.permutations(map(str, pool), M)))
for i in permute:
    print(i)
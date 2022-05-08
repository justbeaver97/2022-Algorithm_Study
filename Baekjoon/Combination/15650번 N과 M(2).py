"""
15650번 - https://www.acmicpc.net/problem/15650

N과 M(2)

reference 
combintation 
"""

import itertools

N, M = map(int,input().split())
permute = list(map(' '.join, itertools.combinations(map(str, range(1,N+1)), M)))
print('\n'.join(permute))
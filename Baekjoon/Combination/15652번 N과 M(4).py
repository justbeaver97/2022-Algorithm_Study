"""
15651번 - https://www.acmicpc.net/problem/15651

N과 M(3)

reference
combinations_with_replacement - https://soundprovider.tistory.com/entry/python-itertools
"""

import itertools

N, M = map(int,input().split())
permute = list(map(' '.join, itertools.combinations_with_replacement(map(str, range(1,N+1)), M)))
print('\n'.join(permute))
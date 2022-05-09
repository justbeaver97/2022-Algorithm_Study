"""
15651번 - https://www.acmicpc.net/problem/15651

N과 M(3)

reference
product - https://soundprovider.tistory.com/entry/python-itertools
"""

import itertools

N, M = map(int,input().split())
permute = list(map(' '.join, itertools.product(map(str, range(1,N+1)), repeat=M)))
print('\n'.join(permute))
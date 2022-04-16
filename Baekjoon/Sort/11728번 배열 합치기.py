"""
11728번 - https://www.acmicpc.net/problem/11728

배열 합치기

reference
print(' '.join()) - https://naekang.tistory.com/64
"""

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print(' '.join(map(str, sorted(arr1+arr2))))
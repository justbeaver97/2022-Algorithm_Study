"""
1920번 - https://www.acmicpc.net/problem/1920

수 찾기
"""

import sys
input = sys.stdin.readline

def found(num):
    start, end = 0, N-1
    while start <= end:
        mid = (start+end)//2
        if num == list_n[mid]:  return True
        elif num > list_n[mid]: start = mid + 1
        else:                   end = mid - 1
    return False

N = int(input())
list_n = sorted(list(map(int,input().split())))
M = int(input())
list_m = list(map(int,input().split()))

for num in list_m:
    if found(num): print(1)
    else:          print(0)
"""
15965번 - https://www.acmicpc.net/problem/15965

K번째 소수
"""

import sys
input = sys.stdin.readline

K = int(input())
prime, arr = [False, False] + [True]*(10**7-1), []
for i in range(2, len(prime)):
    if prime[i]:
        arr.append(i)
        for j in range(i*i,len(prime), i):
            prime[j] = False
print(arr[K-1])

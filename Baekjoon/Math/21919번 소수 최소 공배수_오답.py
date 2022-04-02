"""
21919번 - https://www.acmicpc.net/problem/21919

소수 최소 공배수

행복이는 길이가 N인 수열 A에서 소수들을 골라 최소공배수를 구해보려고 한다.
행복이를 도와 이를 계산해주자.
"""

import sys
input = sys.stdin.readline

def GCD(x,y):
    tmp = x % y
    while y != 0:
        tmp = x % y
        x = y
        y = tmp
    return x

is_prime = [False,False]+[True]*(1000000-1)
for i in range(2,len(is_prime)):
    if is_prime[i]:
        for j in range(i*2, len(is_prime), i):
            if is_prime[j]:
                is_prime[j]=False
            
N = int(input())
A = list(map(int, input().split()))
arr = []

for num in A:
    if is_prime[num]:
        arr.append(num)

if arr == []:
    print(-1)
else:
    lcm = arr[0]
    for i in range(1,len(arr)):
        if lcm > arr[i]:
            lcm = (lcm * arr[i]) / GCD(lcm, arr[i])
        else:
            lcm = (lcm * arr[i]) / GCD(arr[i],lcm)
    print(int(lcm))
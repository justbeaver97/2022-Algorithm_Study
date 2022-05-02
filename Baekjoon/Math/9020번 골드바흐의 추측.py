"""
9020번 - https://www.acmicpc.net/problem/9020

골드바흐의 추측

처음에 틀린 이유
for i in range(n//2,2,-1) 로 설정해주면서, 3까지만 searching함
4 = 2 + 2 같은 케이스에서 틀린듯
"""  

import sys
input = sys.stdin.readline

def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        # print(num, i)
        if num % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(n//2,1,-1):
        if is_prime(i) and is_prime(n-i):
            print(f"{i} {n-i}")
            break
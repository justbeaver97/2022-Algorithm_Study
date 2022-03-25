"""
5347번 - https://www.acmicpc.net/problem/5347

LCM

두 수 a와 b가 주어졌을 때, a와 b의 최소 공배수를 구하는 프로그램을 작성하시오
"""

import sys
input = sys.stdin.readline

def GCD(a, b):
    tmp = a % b
    while b != 0 :
        tmp = a % b
        a = b
        b = tmp
    return a

def LCM(x, y):
    if x > y:
        gcd = GCD(x,y)
        print(int((x*y)/gcd))
    else:
        gcd = GCD(y,x)
        print(int((x*y)/gcd))

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    LCM(x,y)
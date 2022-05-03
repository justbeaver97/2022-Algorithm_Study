"""
9655번 - https://www.acmicpc.net/problem/9655

돌 게임
"""  

import sys
input = sys.stdin.readline

N = int(input())
print("CY") if N % 2 ==0 else print("SK")

"""
12847번 - https://www.acmicpc.net/problem/12847

꿀 아르바이트
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
payments = list(map(int, input().split()))

sliding_window = sum(payments[:m])
best_pay = sliding_window
for i in range(m,n):
    sliding_window = sliding_window + payments[i] - payments[i-m]
    best_pay = max(best_pay, sliding_window)
print(best_pay)
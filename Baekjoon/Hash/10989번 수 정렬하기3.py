"""
10989번 - https://www.acmicpc.net/problem/10989

수 정렬하기3

오답 이유 - 메모리 초과
아래에 있는 오답의 경우 list로 치면 append를 해나가는 방식
처음에 필요한 list의 크기를 정해놓고 list에 필요한 value를 집어넣는 방식이 memory가 적게 든다
"""

import sys
input = sys.stdin.readline

N = int(input())
numbers = {}
for i in range(N):
    tmp = int(input())
    numbers[i] = tmp
for i in sorted(numbers.values()):
    print(i)
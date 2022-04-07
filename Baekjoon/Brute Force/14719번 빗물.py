"""
14719번 - https://www.acmicpc.net/problem/14719

빗물
2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

22/04/05 BOJ 2304번. 창고 다각형 
https://github.com/justbeaver97/2022-Paper_Review_Algorithm_Study/blob/main/Baekjoon/Brute%20Force/2304%EB%B2%88%20%EC%B0%BD%EA%B3%A0%20%EB%8B%A4%EA%B0%81%ED%98%95.py
과 유사한 문제

풀이방법:
좌측에서 오면서 가장 큰 block을 update하는 list
우측에서 오면서 가장 큰 block을 update하는 list
area += index별 가장 큰 block - 해당 index 실제 block
"""

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int,input().split()))
highest_block = max(blocks)
highest_index = blocks.index(highest_block)
from_left, from_right, area = [], [], 0

if highest_index > 0: 
    from_left.append(blocks[0])
    for i in range(1,highest_index):
        if blocks[i] > from_left[i-1]: from_left.append(blocks[i])
        else:                          from_left.append(from_left[i-1])
if highest_index != W-1:
    from_right.append(blocks[-1])
    for i in range(W-2,highest_index,-1):
        if blocks[i] > from_right[W-i-2]: from_right.append(blocks[i])
        else:                             from_right.append(from_right[W-i-2])

if from_left != []:
    for i in range(0,highest_index):
        area += from_left[i] - blocks[i]
if from_right != []:
    for i in range(W-1, highest_index, -1):
        area += from_right[W-i-1] - blocks[i]
print(area)
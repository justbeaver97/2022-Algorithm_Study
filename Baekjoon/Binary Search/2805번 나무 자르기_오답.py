"""
2805번 - https://www.acmicpc.net/problem/2805

나무 자르기

오답 이유 - Runtime Error
이분 탐색을 사용하지 않고 brute force 하게 문제를 진행
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

cut_tree, highest_tree = 0, max(trees)
while cut_tree < M:
    for i in range(N):
        if trees[i] > highest_tree-1:
            trees[i] -= 1
            cut_tree += 1
    highest_tree -= 1
print(highest_tree)
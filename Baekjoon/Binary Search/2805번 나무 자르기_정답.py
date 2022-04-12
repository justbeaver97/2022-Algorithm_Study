"""
2805번 - https://www.acmicpc.net/problem/2805

나무 자르기
"""

import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
lowest, highest = 0, max(trees)

while lowest <= highest:
    median, cut_tree = (lowest+highest)//2, 0

    for tree in trees:
        if tree > median:
            cut_tree += tree - median

    if cut_tree >= M: lowest = median + 1
    else:             highest = median - 1
print(highest)

"""
while answer != median:
    median, cut_tree = (lowest+highest)//2, 0

    for i in range(N):
        if trees[i] > median:
            cut_tree += trees[i] - median

    if cut_tree == M:  answer = median
    elif cut_tree > M: lowest = median - 1
    else:         highest = median +1
print(answer)
"""
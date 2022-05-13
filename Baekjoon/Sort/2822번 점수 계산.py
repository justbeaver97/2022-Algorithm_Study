"""
5635번 - https://www.acmicpc.net/problem/5635

생일
"""

import sys
input = sys.stdin.readline

scores = [0]+[int(input()) for _ in range(8)]
total_score, score_index = 0, []

for i in range(5):
    maximum_score = max(scores)
    total_score += maximum_score
    maximum_score_index = scores.index(maximum_score)
    score_index.append(maximum_score_index)
    scores[maximum_score_index] = 0
print(f"{total_score}\n{' '.join(map(str,sorted(score_index)))}")
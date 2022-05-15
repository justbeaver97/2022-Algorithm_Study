"""
1015번 - https://www.acmicpc.net/problem/1015

수열 정렬

틀린 이유
문제 조건이 "배열의 원소는 1,000보다 작거나 같은 자연수이다"인데
1000보다 작다고 이해하고 문제를 풀었음
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = [N] * N
for i in range(N):
    min_num_index = arr.index(min(arr))
    answer[min_num_index] = i
    arr[min_num_index] = 1001
print(' '.join(map(str,answer)))
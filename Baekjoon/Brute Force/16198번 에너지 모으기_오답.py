"""
16198번 - https://www.acmicpc.net/problem/16198

에너지 모으기

오답
5 
3 1 2 4 5
오답: 31, 정답: 33

8
10 7 8 9 10 2 4 13
오답: 570, 정답: 612

이유: 가장 큰값을 더해나가도 이 값들의 합이 최고값이 아닐 수 있다
"""

import sys
input = sys.stdin.readline

N = int(input())
W = list(map(int, input().split()))
energy = 0

for _ in range(N-2):
    tmp, tmp_index = 0, 1
    for i in range(1, len(W)-1):
        if W[i-1]*W[i+1] > tmp:
            tmp = W[i-1]*W[i+1]
            tmp_index = i
        elif W[i-1]*W[i+1] == tmp: 
            if W[tmp_index] > W[i]:
                tmp_index = i
    del W[tmp_index]
    energy += tmp
print(energy)
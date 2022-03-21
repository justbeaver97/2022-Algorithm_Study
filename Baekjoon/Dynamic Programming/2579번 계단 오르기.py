"""
2579번 - https://www.acmicpc.net/problem/2579

계단 오르기


1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.

오답이유
max_num[2]를 잘못 선언함
"""

import sys 
input = sys.stdin.readline

n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0]+stair[1])
else:
    max_sum = [0]*n
    max_sum[0] = stair[0]
    max_sum[1] = stair[1]+stair[0]
    max_sum[2] = max(stair[2]+stair[0],stair[2]+stair[1])

    for i in range(3,n):
        max_sum[i] = stair[i]+ max(stair[i-1]+max_sum[i-3], max_sum[i-2])

    print(max_sum[-1])
"""
14501번 - https://www.acmicpc.net/problem/14501

퇴사
"""

import sys
input = sys.stdin.readline

N = int(input())
consultings = list(list(map(int,input().split())) for _ in range(N)) 
dp = [0 for _ in range(N)] + [0]

for i in range(N-1,-1,-1):
    day, pay = consultings[i]

    ## i+x일 후가 퇴사 이후면 그냥 앞날의 값 가져옴
    if day + i > N: dp[i] = dp[i+1]
    ## 앞날 vs 오늘 pay + (i+x)의 pay
    else: dp[i] = max(dp[i+1], pay + dp[i+day])
print(dp[0])
"""
21921번 - https://www.acmicpc.net/problem/21921

블로그

오답 이유 - 틀렸습니다
max_range를 1이 아닌 0으로 시작
-> 애초에 max(visitors)==0일때를 제외한 경우이기 때문에
-> max_range를 1로 시작하는 것이 맞음
"""

import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

if max(visitors) == 0:
    print("SAD")
else:
    sliding_window = sum(visitors[:X])
    max_num, max_range = sliding_window, 1
    for i in range(X,N):
        sliding_window += visitors[i]
        sliding_window -= visitors[i-X]

        if sliding_window > max_num:
            max_num = sliding_window
            max_range = 1
        elif sliding_window == max_num and sliding_window != 0:
            max_range += 1
    print(f"{max_num}\n{max_range}") 

"""
sliding_window = sum(visitors[:X])
max_num, max_range = sliding_window, 0
for i in range(X,N):
    sliding_window += visitors[i]
    sliding_window -= visitors[i-X]

    if sliding_window > max_num:
        max_num = sliding_window
        max_range = 1
    elif sliding_window == max_num and sliding_window != 0:
        max_range += 1
print(f"{max_num}\n{max_range}") if max_range != 0 else print("SAD")
"""
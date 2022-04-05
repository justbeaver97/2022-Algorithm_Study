"""
2304번 - https://www.acmicpc.net/problem/2304

창고 다각형

reference
1. max + lambda
https://velog.io/@aonee/Python-%EB%9E%8C%EB%8B%A4-lambda
2. lambda 조건 2개
https://dailyheumsi.tistory.com/67

오답 이유 - 중간에 풀다가 멈춤
가장 큰 기둥이 2개일때를 고려 X
7
3 2
2 1
1 4
6 2
4 3
5 1
7 1
"""

import sys
input = sys.stdin.readline

def print_area(pillars, highest_pillar):
    highest_index, area = pillars.index(highest_pillar), 0
    if highest_index > 0:
        for i in range(1,highest_index+1):
            area += (pillars[i][0]-pillars[i-1][0]) * pillars[i-1][1]
    if highest_index != len(pillars)-1:
        for i in range(len(pillars)-1,highest_index,-1):
            area += (pillars[i][0]-pillars[i-1][0]) * pillars[i][1]
    area += pillars[highest_index][1]
    print(area)

N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)])
highest_pillar = max(arr, key= lambda x:x[1])
highest = arr.index(highest_pillar)
pillars = [arr[0]]

## 가장 높은 기둥 이전, 첫번째가 가장 높은 기둥이면 실행 X
if highest > 0:
    for i in range(1,highest+1):
        ## 가장 끝점이 가장 큰 경우
        if i == N-1:
            pillars.append([arr[i][0],arr[i][1]])
            continue
        ## 기존에 있는 기둥보다 더 큰 기둥이 나오면 append
        if arr[i][1] > pillars[len(pillars)-1][1]:
            pillars.append(arr[i])
tmp_arr = arr[highest+1:]

## 가장 높은 기둥 이후, 마지막이 가장 높은 기둥이면 실행 X
if highest != N-1:
    ## y descend, x descend
    sort_tmp_arr = sorted(tmp_arr, key = lambda x : (-x[1],-x[0]))
    
    tmp1, tmp2 = sort_tmp_arr[0][0], sort_tmp_arr[0][1] # x, y
    for i in range(1,len(sort_tmp_arr)):

        ## x가 더 큰데 y가 더 작으면 pillar에 append
        if sort_tmp_arr[i][0] > tmp1 and sort_tmp_arr[i][1] < tmp2:
            if sort_tmp_arr[0][0] == tmp1 and sort_tmp_arr[0][1] == tmp2:
                pillars.append([tmp1,tmp2])
            tmp1, tmp2 = sort_tmp_arr[i][0], sort_tmp_arr[i][1]
            pillars.append([tmp1, tmp2])

        ## 가장 마지막이 2번째로 큰 경우
        if i == len(sort_tmp_arr)-1:
            if sort_tmp_arr[0][0] == tmp1 and sort_tmp_arr[0][1] == tmp2:
                pillars.append([tmp1,tmp2])
    if len(sort_tmp_arr) == highest:
        pillars.append([sort_tmp_arr[0][0],sort_tmp_arr[0][1]])

print_area(pillars, highest_pillar)
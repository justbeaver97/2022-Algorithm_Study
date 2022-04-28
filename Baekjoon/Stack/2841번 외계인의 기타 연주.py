"""
2841번 - https://www.acmicpc.net/problem/2841

외계인의 기타 연주
5 15
2 8
2 10
2 12
2 10
2 5
"""

import sys
input = sys.stdin.readline

N, P = map(int, input().split())
arr, answer = [[] for _ in range(7)], 0
for i in range(N):
    line_num, pret_num = map(int,input().split())
    if len(arr[line_num]) == 0:
        arr[line_num].append(pret_num)
        answer += 1
    else:
        if pret_num > arr[line_num][-1]:
            arr[line_num].append(pret_num)
            answer += 1
        elif pret_num == arr[line_num][-1]:
            continue
        else:
            while True:
                if len(arr[line_num])!=0 and arr[line_num][-1] == pret_num:
                    break
                elif len(arr[line_num])==0 or arr[line_num][-1]<pret_num:
                    arr[line_num].append(pret_num)
                    answer +=1
                    break
                arr[line_num].pop()
                answer += 1
print(answer)
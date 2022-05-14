"""
1065번 - https://www.acmicpc.net/problem/1065

한수
"""

import sys
input = sys.stdin.readline

N = int(input())
answer = 0

for i in range(1,N+1):
    tmp = list(str(i))
    if len(tmp) < 3:
        answer += 1
    else:
        diff, count = int(tmp[0])-int(tmp[1]), 0
        for j in range(1,len(tmp)-1):
            if int(tmp[j])-int(tmp[j+1]) == diff:
                count += 1
        if count == len(tmp)-2:
            answer += 1
print(answer)
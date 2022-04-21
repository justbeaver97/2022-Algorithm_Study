"""
1431번 - https://www.acmicpc.net/problem/1431

시리얼 번호

reference
1. dictionary 다중 value - 사용 X
https://leti-lee.tistory.com/15

2. dictonary 다중 sort(대신 list 안에 dict가 들어가는 형태)
https://jeongmin-lee.tistory.com/82

3. isdigit()
https://infinitt.tistory.com/252
"""

import sys
input = sys.stdin.readline

N = int(input())
serials = []
for _ in range(N):
    tmp = input().rstrip('\n')
    list_tmp, sum = list(tmp), 0
    for n in list_tmp:
        if n.isdigit():
            sum += int(n)
    serials.append({'number':tmp, 'length':len(tmp), 'sum': sum})
sorted_serials = sorted(serials, key = lambda x: (x['length'], x['sum'],x['number']))
for i in sorted_serials:
    print(i['number'])
"""
1074번 - https://www.acmicpc.net/problem/1074

Z
"""

import sys
input = sys.stdin.readline

N, r, c = map(int,input().split())
answer = 0
while N != 0:
    N -= 1

    if r < (2**N) and c < (2**N):
        pass
    elif r < (2**N) and c >= (2**N):
        answer += (2**N)**2
        c -= (2**N)
    elif r >= (2**N) and c < (2**N):
        answer += ((2**N)**2) * 2
        r -= (2**N)
    else:
        answer += ((2**N)**2) * 3
        r -= (2**N)
        c -= (2**N)
if r == 0 and c == 0:   print(answer)
elif r == 0 and c == 1: print(answer+1)
elif r == 1 and c == 0: print(answer+2)
else:                   print(answer+3)
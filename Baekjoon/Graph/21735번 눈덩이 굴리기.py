"""
21735번 - https://www.acmicpc.net/problem/21735

눈덩이 굴리기
"""

import sys
input = sys.stdin.readline

def DFS(index, time, size):
    global answer
    
    ## 시간 초과
    if time > M:  return 
    ## 눈덩이 중 더 큰 값을 저장
    if time <= M: answer = max(answer, size)

    ## 눈덩이를 굴리기
    if index <= N-1: DFS(index+1, time+1, size+snows[index+1])
    ## 눈덩이를 던지기
    if index <= N-2: DFS(index+2, time+1, size//2+snows[index+2])

N, M = map(int, input().split())
snows, answer = [0]+list(map(int, input().split())), -1
DFS(0,0,1)
print(answer)
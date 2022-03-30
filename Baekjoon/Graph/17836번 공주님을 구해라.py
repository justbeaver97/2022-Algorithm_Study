"""
17836번 - https://www.acmicpc.net/problem/17836

공주님을 구해라!
"""

import sys
import collections
input = sys.stdin.readline

def BFS():
    a, b = -1, -1
    while queue:
        x, y = queue.popleft()
        for i in range(len(dir)):
            new_x, new_y= x + dir[i][0], y + dir[i][1]
            if 0<=new_x<N and 0<=new_y<M  and (arr[new_x][new_y]==0 or arr[new_x][new_y]==2):
                if arr[new_x][new_y]==2:
                    a, b = new_x, new_y
                arr[new_x][new_y] = arr[x][y] - 1
                queue.append((new_x,new_y))
    return a, b

N, M, T = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dir = [[1,0],[-1,0],[0,-1],[0,1]]

queue = collections.deque()
queue.append([0,0])
sword_x, sword_y = BFS()

if sword_x!=-1 and sword_y!=-1 :
    ## 검이 있음에도 공주까지 못 갔을때
    if arr[N-1][M-1] == 0:
        arr[N-1][M-1] = arr[sword_x][sword_y]-(M-1-sword_x + N-1-sword_y)

    ## 검에서 간 거리랑, 그냥 간 거리 비교했을 때
    elif (arr[sword_x][sword_y]-(M-1-sword_x + N-1-sword_y)) > arr[N-1][M-1]:
        arr[N-1][M-1] = arr[sword_x][sword_y]-(M-1-sword_x + N-1-sword_y)

## 최종적으로 도달하지 못했거나, 갔더라도 공주가 죽었을 때
if arr[N-1][M-1] == 0 or abs(arr[N-1][M-1]) > T:
    print("Fail")
else:
    print(abs(arr[N-1][M-1]))

"""
7569번 - https://www.acmicpc.net/problem/7569

토마토

전부 다 익는데 걸리는 시간은 BFS를 했을 때 저장된 가장 마지막 수 - 1
"""

import collections

def BFS():
    while queue:
        x, y, z = queue.popleft()
        for i in range(len(dir)):
            new_x, new_y, new_z = x + dir[i][0], y + dir[i][1], z+dir[i][2]
            if 0<= new_x <h and 0<= new_y <n and 0<= new_z <m and tomato[new_x][new_y][new_z]==0:
                tomato[new_x][new_y][new_z] = tomato[x][y][z] + 1
                queue.append((new_x,new_y,new_z))


## m: 상자의 가로 칸 수, n: 상자의 세로 칸 수, h: 쌓아올려지는 상자의 수
m, n, h = map(int, input().split())

## 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
tomato = []
for _ in range(h):
    tmp_arr = []
    for _ in range(n):
        tmp = list(map(int,input().split()))
        tmp_arr.append(tmp)
    tomato.append(tmp_arr)

dir = [[1,0,0],[-1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]
queue = collections.deque()

for i in range(h):
    for j in range(n):
        for k in range(m):    
            if tomato[i][j][k] == 1:
                queue.append([i,j,k])
BFS()

ripe_tomato, raw_tomato = 0, False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                raw_tomato = True
            if tomato[i][j][k] > ripe_tomato:
                ripe_tomato = tomato[i][j][k]

if raw_tomato == True:
    print(-1)
elif ripe_tomato == 1:
    print(0)
else:
    print(ripe_tomato-1)
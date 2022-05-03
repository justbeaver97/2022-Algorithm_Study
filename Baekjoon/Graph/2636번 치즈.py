"""
2636번 - https://www.acmicpc.net/problem/2636

치즈

처음에 안 풀린 이유
width와 heigth가 다른 경우 x,y를 y,x로 접근해야함. 
나는 x,y로 접근했기 때문에 
0<= new_x <width and 0<= new_y <height
가 아닌
0<= new_x <height and 0<= new_y <width
로 접근해야했음
""" 

import sys, collections
input = sys.stdin.readline

def BFS():
    queue, tmp = collections.deque(), 0
    queue.append((0,0))

    while queue:
        x, y = queue.popleft()
        for i in range(len(dir)):
            new_x, new_y = x + dir[i][0], y + dir[i][1]

            if 0<= new_x <height and 0<= new_y <width and not tmp_arr[new_x][new_y]:
                if arr[new_x][new_y] == 0:
                    tmp_arr[new_x][new_y] = True
                    queue.append((new_x,new_y))
                else:
                    tmp += 1
                    arr[new_x][new_y] = 0
                    tmp_arr[new_x][new_y] = True
    answer.append(tmp)
    return tmp

height, width = map(int, input().split())
arr = list(list(map(int,input().split())) for _ in range(height))
dir, answer, tmp, time = [[-1,0],[1,0],[0,1],[0,-1]], [], 1, 0

while tmp != 0:
    time += 1
    tmp_arr = [[False]*width for _ in range(height)]
    tmp = BFS()
print(f"{time-1}\n{answer[-2]}")
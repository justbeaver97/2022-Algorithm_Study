"""
17836번 - https://www.acmicpc.net/problem/17836

오목, 이길 수 있을까?

구사과와 큐브러버는 10×10 크기의 바둑판에서 오목을 하고 있다. 턴은 구사과가 먼저 갖는다. 
바둑판의 상태가 주어진다. 구사과가 턴을 한 번 더 가졌을 때, 이길 수 있는지 구하는 프로그램을 작성하시오.

오목에서 승리했다는 것은 자신의 돌이 5개 이상 연속한다는 것이다. 연속은 가로, 세로, 대각선 방향 모두 가능하다.

sort 2가지
https://dailyheumsi.tistory.com/67

틀린 이유
1. 문제에서 주어진 상황대로 돌이 각각 4개만 있었을 것이라 판단
2. tmp_arr= arr[:] 라고 해주었음에도 arr가 tmp_arr를 수정하면 같이 바뀌는 현상 발생
-> 내가 알기로 slicing을 쓰면 shallow copy인데 왜?
-> 따라서, arr가 계속 바뀌면서 돌을 놓을 수 있는 경우를 각각 따지는게 아니라 모두 한꺼번에 놓고 따지게 됨
"""

import sys
import collections
input = sys.stdin.readline
queue, queue2 =  collections.deque(), collections.deque()

def BFS():
    x, y = queue.popleft()
    for i in range(len(dir)):
        new_x = x + dir[i][0]
        new_y = y + dir[i][1]
        if 0<=new_x<10 and 0<=new_y<10 and tmp_arr[new_x][new_y]==".":
            new_coors.append([new_x, new_y])
            tmp_arr[new_x][new_y] = "X"

# def BFS_can_win():
#     count = 0
#     while queue2:
#         x, y = queue2.popleft()
#         for i in range(len(win_dir)):
#             new_x = x + win_dir[i][0]
#             new_y = y + win_dir[i][1]
#             if 0<=new_x<10 and 0<=new_y<10 and tmp_arr2[new_x][new_y]=="X":
#                 queue2.append([new_x,new_y])
#                 tmp_arr2[new_x][new_y] = "."
#                 count += 1
#     return count

coors, arr = [],[]
dir = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

for i in range(10):
    tmp = list(input().rstrip())
    arr.append(tmp)
    for j in range(10):
        if tmp[j] == "X":
            coors.append([i,j])

can_win = False
for i in range(4):
    tmp_arr, new_coors = arr[:], []
    queue.append(coors[i])
    BFS()
    
    for j in range(len(new_coors)):
        tmp_coors = coors[:]
        tmp_coors.append(new_coors[j])
        tmp_coors = sorted(tmp_coors, key = lambda x: (x[0],x[1]))
        z, w = tmp_coors[1][0] - tmp_coors[0][0], tmp_coors[1][1] - tmp_coors[0][1]
        print("j",tmp_coors,z,w)
        for k in range(1,len(tmp_coors)-1):
            # print("k",tmp_coors[k+1][0] - tmp_coors[k][0],tmp_coors[k+1][1] - tmp_coors[k][1])
            if z != tmp_coors[k+1][0] - tmp_coors[k][0] or w != tmp_coors[k+1][1] - tmp_coors[k][1]:
                print("k",tmp_coors[k+1][0] - tmp_coors[k][0],tmp_coors[k+1][1] - tmp_coors[k][1])
                can_win = False
                break
            else: can_win = True
        if can_win:
            print(1)
            exit()
print(0)

# for i in range(4):
#     tmp_arr, new_coors = arr[:], []
#     queue.append(coors[i])
#     BFS()
#     for j in range(len(new_coors)):
#         tmp_arr2 = tmp_arr[:]
#         z = new_coors[j][0] - coors[i][0]
#         w = new_coors[j][1] - coors[i][1]
#         # print(new_coors[j], coors[i])
#         win_dir = [[z,w],[-z,-w]]
#         # print(win_dir)
#         queue2.append(new_coors[j])
#         answer = BFS_can_win()
#         if answer == 5:
#             print(1)
#             exit()
# print(0)
"""
17836번 - https://www.acmicpc.net/problem/17836

오목, 이길 수 있을까?

구사과와 큐브러버는 10×10 크기의 바둑판에서 오목을 하고 있다. 턴은 구사과가 먼저 갖는다. 
바둑판의 상태가 주어진다. 구사과가 턴을 한 번 더 가졌을 때, 이길 수 있는지 구하는 프로그램을 작성하시오.

오목에서 승리했다는 것은 자신의 돌이 5개 이상 연속한다는 것이다. 연속은 가로, 세로, 대각선 방향 모두 가능하다.

reference
1. deepcopy 
https://black-hair.tistory.com/49

"""

import sys
import copy
import collections
input = sys.stdin.readline
queue, queue2 =  collections.deque(), collections.deque()

def BFS():
    x, y = queue.popleft()
    tmp_arr = copy.deepcopy(arr)
    for i in range(len(dir)):
        new_x = x + dir[i][0]
        new_y = y + dir[i][1]

        ## 돌이 우선적으로 놓여져 있는 곳에서 8가지 방향에 놓는 것을 모두 고려
        if 0<=new_x<10 and 0<=new_y<10 and tmp_arr[new_x][new_y]==".":
            tmp_arr = copy.deepcopy(arr)
            tmp_arr[new_x][new_y] = "X"
            # print(f"2  x{x} y{y} {new_x} {new_y} {tmp_arr}")

            ## 만약 돌을 놓게 된다면, 해당 돌에서 new_dir 방향으로 5번 연속 갈 수 있는지 판단
            ## dir 가 아닌 new_dir인 이유는, 상하/좌우로 훑기 때문에
            for j in range(10):
                for k in range(10):
                    if tmp_arr[j][k] == "X":
                        # print(f"3  j{j} k{k}")
                        for l in range(4):
                            count = 1
                            nx, ny = j, k

                            ## 해당 바둑판에서 5번 연속으로 오목이 있는지 검색
                            for m in range(5):
                                nx += win_dir[l][0]
                                ny += win_dir[l][1]
                                # print(f"4  nx{nx} ny{ny}", end='  ')
                                if 0<=nx<10 and 0<=ny<10 and tmp_arr[nx][ny]=="X":
                                    # print(f"5  nx{nx} ny{ny}")
                                    count += 1
                                else:
                                    count = 1
                                    break
                                if count == 5:
                                    return True

coors, arr = [],[]
dir = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

for i in range(10):
    tmp = list(input().rstrip())
    arr.append(tmp)
    for j in range(10):
        if tmp[j] == "X":
            coors.append([i,j])

can_win = False
win_dir = [[-1,1],[0,1],[1,1],[1,0]]
for i in range(len(coors)):
    queue.append(coors[i])
    if BFS():
        print(1)
        exit()
print(0)
"""
16948번 - https://www.acmicpc.net/problem/16948

게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
크기가 NxN인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다.
데스 나이트는 체스판 밖으로 벗어날 수 없다.

reference
이차원 배열 한줄로 만들기 - https://dojang.io/mod/page/view.php?id=2293
bfs 최단거리 구하기 - https://steadily-worked.tistory.com/497 
"""

import collections 

def bfs(x,y):
    queue = collections.deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(len(dir)):
            new_x, new_y = x + dir[i][0], y + dir[i][1]

            if 0<= new_x <n and 0<= new_y <n and arr[new_x][new_y]==0:
                arr[new_x][new_y] = arr[x][y] + 1
                queue.append((new_x,new_y))
                if new_x == r2 and new_y == c2:
                    return arr[r2][c2]
    return -1


n = int(input())
r1, c1, r2, c2 = map(int, input().split())

arr = [[0] * n for _ in range(n)]
dir = [[-2,-1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]
print(bfs(r1,c1))
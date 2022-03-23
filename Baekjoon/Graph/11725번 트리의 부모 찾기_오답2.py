"""
11725번 - https://www.acmicpc.net/problem/11725

트리의 부모 찾기

루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

오답 이유
메모리 초과 이유 - https://d-cron.tistory.com/22 
노드의 개수가 100,000 개까지 가능하므로, 2차원 배열로 선언하게 되면 100,000 * 100,000 -> 메모리 초과
"""

import sys
import collections
input = sys.stdin.readline
N = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

queue = collections.deque()
queue.append(1)
for i in range(1,N+1):
    row = queue.popleft()
    for j in range(1,N+1):
        if graph[row][j] == 1 and graph[j][row] == 1:
            graph[j][row] = 0
            queue.append(j)

arr = [[-1] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j] == 1:
            arr[j].append(i)

for item in arr:
    item.remove(-1)
    
for i in range(2, N+1):
    print(arr[i][0])
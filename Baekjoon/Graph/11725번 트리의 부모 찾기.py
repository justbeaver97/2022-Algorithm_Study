"""
11725번 - https://www.acmicpc.net/problem/11725

트리의 부모 찾기

루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
"""

import sys
import collections

def BFS():
    while queue:
        num = queue.popleft()
        for i in graph[num]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = num

input = sys.stdin.readline
N = int(input())
graph = [[0] for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (N+1)
queue = collections.deque([1])
BFS()

for item in visited[2:]:
    print(item)
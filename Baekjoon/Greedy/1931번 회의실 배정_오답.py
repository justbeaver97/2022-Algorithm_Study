"""
1931번 - https://www.acmicpc.net/problem/1931

회의실 배정

한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

오답이유:
꼭 끝 시간과 시작 시간이 이어져 있을 필요가 없음에도 문제를 BFS 적으로 생각
"""

import sys 
import collections
input = sys.stdin.readline

def BFS(graph, visited, start):
    queue = collections.deque([start])
    visited[start] += 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] += 1
                

n = int(input())
meet, max_hour = [], 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    meet.append(tmp)
    if tmp[1] > max_hour:
        max_hour = tmp[1]

## [[-1, 6], [-1, 4], [-1, 13], [-1, 5, 8], [-1], [-1, 7, 9], [-1, 10], [-1], [-1, 11, 12], [-1], [-1], [-1], [-1, 14], [-1], [-1]]
graph = [[-1] for _ in range(max_hour+1)]
for i in range(n):
    graph[meet[i][0]].append(meet[i][1])

## [[6], [4], [13], [5, 8], [], [7, 9], [10], [], [11, 12], [], [], [], [14], [], []]
for item in graph:
    item.remove(-1)

for i in range(max_hour+1):
    visited = [0] * (max_hour+1)
    BFS(graph, visited, i)
    print(i, visited)
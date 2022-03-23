"""
11725번 - https://www.acmicpc.net/problem/11725

트리의 부모 찾기

루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

오답 이유
모든 노드가 순차적으로 들어올 것이라고 생각
1 3
2 4
4 2
이런 식으로도 들어올 수 있음
"""

import sys
input = sys.stdin.readline

N = int(input())
graph = [[-1] for _ in range(N+1)]
graph[1] = []

# for _ in range(N-1):
#     node1, node2 = map(int, input().split())

#     if graph[node1] != [-1]:
#         graph[node1].append(node2)
#         if graph[node2] == [-1]:
#             graph[node2] = []
#     elif graph[node2] != [-1]:
#         graph[node2].append(node1)
#         if graph[node1] == [-1]:
#             graph[node1] = []

for _ in range(N-1):
    node1, node2 = map(int, input().split())

    if graph[node1] != [-1]:
        if graph[node2] == [-1]:
            graph[node2] = []
        graph[node2].append(node1)
    elif graph[node2] != [-1]:
        if graph[node1] == [-1]:
            graph[node1] = []
        graph[node1].append(node2)
print(graph)

for i in range(2,N+1):
    print(graph[i][0])
"""
11403번 - https://www.acmicpc.net/problem/11403 

경로 찾기
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

reference
인접행렬 - https://sarah950716.tistory.com/12 
"""

def DFS(v):
    visited[v]=True
    for num in connected[v]:
        result.append(num)
        if visited[num]==False:
            DFS(num)
            

n = int(input())
graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

connected = [[-1] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            connected[i].append(j)
for item in connected:
    item.remove(-1)

final = []
for i in range(n):
    result = []
    visited = [False]*(n+1)
    DFS(i)
    final.append(result)

for i in range(len(final)):
    for num in final[i]:
        graph[i][num] = 1

for i in range(len(graph)):
    for j in range(len(graph)):
        if j == len(graph)-1:
            print(graph[i][j])
        else:
            print(graph[i][j],end=' ')
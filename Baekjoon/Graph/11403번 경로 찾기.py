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
        # 연결된 노드가 이미 방문한 노드일 수도 있으므로(ex 자기자신) if문 전에 num을 append 해준다
        result.append(num)
        if visited[num]==False:
            DFS(num)
            # result.append(num)
            

n = int(input())
graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

# [[-1, 3], [-1, 6], [-1], [-1, 4, 5], [-1, 0], [-1, 6], [-1, 2]] - 이런 그래프를 만든다
connected = [[-1] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            connected[i].append(j)

# [[3], [6], [], [4, 5], [0], [6], [2]] - -1을 제거하여 방향성을 가진 인접행렬의 그래프로 나타내준다
for item in connected:
    item.remove(-1)

# [[3, 4, 0, 5, 6, 2], [6, 2], [], [4, 0, 3, 5, 6, 2], [0, 3, 4, 5, 6, 2], [6, 2], [2]] 
# 하나의 노드에서 갈 수 있는 모든 노드를 저장한다
final = []
for i in range(n):
    result = []
    visited = [False]*(n+1)
    DFS(i)
    final.append(result)

# final을 토대로 graph를 update 해준다
for i in range(len(final)):
    for num in final[i]:
        graph[i][num] = 1

# graph를 이쁘게 print 한다
for i in range(len(graph)):
    for j in range(len(graph)):
        if j == len(graph)-1:
            print(graph[i][j])
        else:
            print(graph[i][j],end=' ')
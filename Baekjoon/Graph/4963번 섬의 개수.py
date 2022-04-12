"""
4963번 - https://www.acmicpc.net/problem/4963

섬의 개수

reference
sys.setrecursionlimit() - https://fuzzysound.github.io/sys-setrecursionlimit
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(i,j):
    if i<0 or j<0 or i>=h or j>=w:
        return False
    if arr[i][j] == 1:
        arr[i][j] = 2
        DFS(i,j+1),   DFS(i,j-1)
        DFS(i-1,j),   DFS(i+1,j),
        DFS(i+1,j+1), DFS(i+1,j-1),
        DFS(i-1,j-1), DFS(i-1,j+1)
        return True
    return False

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()
    count = 0
    arr = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if DFS(i,j): 
                count += 1
    print(count)
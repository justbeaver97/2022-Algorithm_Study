"""
2167번 - https://www.acmicpc.net/problem/2167

2차원 배열의 합
2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 
배열의 (i, j) 위치는 i행 j열을 나타낸다.
"""

n, m = map(int, input().split())

arr= []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

k = int(input())
add_range = []
for i in range(k):
    tmp = list(map(int, input().split()))
    add_range.append(tmp)

sum_arr = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        sum_arr[i][j] = sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j - 1] + arr[i - 1][j - 1]

for xy in add_range:
    x1, y1, x2, y2 = xy
    answer = sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1]
    print(answer)
"""
5635번 - https://www.acmicpc.net/problem/5635

생일

틀린 이유
arr = sorted(arr, key=lambda x: (x[3],x[2],x[1]))
로 정의하여 sort가 int가 아닌 string 방식으로 되었음
"""

n = int(input())
arr = [list(input().split()) for _ in range(n)]
arr = sorted(arr, key=lambda x: (int(x[3]),int(x[2]),int(x[1])))
print(f"{arr[-1][0]}\n{arr[0][0]}")
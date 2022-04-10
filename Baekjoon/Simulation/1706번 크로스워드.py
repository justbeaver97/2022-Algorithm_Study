"""
1706번 - https://www.acmicpc.net/problem/1706

크로스워드
"""

import sys
input = sys.stdin.readline

def find_row():
    for i in range(R):
        word = ""
        for j in range(C):
            if arr[i][j] != "#":
                word += arr[i][j]
            if arr[i][j] == "#":
                if len(word) > 1:
                    words.append(word)
                word = ""
        if len(word)>1:
            words.append(word)

def find_column():
    for i in range(C):
        word = ""
        for j in range(R):
            if arr[j][i] != "#":
                word += arr[j][i]
            if arr[j][i] == "#":
                if len(word) > 1:
                    words.append(word)
                word = ""
        if len(word)>1:
            words.append(word)


R, C = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(R)]

words = []
find_row()
find_column()
print(sorted(words)[0])
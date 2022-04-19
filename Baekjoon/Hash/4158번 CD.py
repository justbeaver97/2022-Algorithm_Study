"""
4158번 - https://www.acmicpc.net/problem/4158

CD

reference 
동일 원소 비교 - set intersection 
https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%B9%84%EA%B5%90-%EA%B0%99%EC%9D%80%EA%B0%92-%EB%8B%A4%EB%A5%B8%EA%B0%92set%EC%9E%90%EB%A3%8C%ED%98%95%ED%95%A9%EC%A7%91%ED%95%A9%EA%B5%90%EC%A7%91%ED%95%A9%EC%B0%A8%EC%A7%91%ED%95%A9
"""

import sys
input = sys.stdin.readline

while 1:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        exit()
    cd_n = set([int(input()) for _ in range(N)])
    cd_m = set([int(input()) for _ in range(M)])

    answer = len(cd_n.intersection(cd_m))
    print(answer)
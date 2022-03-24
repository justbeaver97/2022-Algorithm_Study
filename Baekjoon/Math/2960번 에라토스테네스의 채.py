"""
2960번 - https://www.acmicpc.net/problem/2960

에라토스테네스의 체

루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4#/media/%ED%8C%8C%EC%9D%BC:Sieve_of_Eratosthenes_animation.gif 
"""

N, K = map(int, input().split())

arr, prime, count = [False, False]+[True]*(N-1), [], 0

for i in range(2,N+1):
    if arr[i]:
        count += 1
        if count == K: 
            print(i)
            exit()
        for j in range(i*2, N+1, i):
            if arr[j]:
                arr[j] = False
                count += 1
            if count == K: 
                print(j)
                exit()
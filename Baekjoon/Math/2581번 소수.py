"""
2581번 - https://www.acmicpc.net/problem/2581

소수
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
"""

M = int(input())
N = int(input())
is_prime=[False]*(N+1)

for i in range(M,N+1):
    is_True = True
    if i < 2:
        continue
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            is_True = False
            break
    if is_True:
        is_prime[i] = True

if True not in is_prime:
    print(-1)
else:
    arr = []
    for i in range(M, N+1):
        if is_prime[i]:
            arr.append(i)
    print(sum(arr))
    print(arr[0])
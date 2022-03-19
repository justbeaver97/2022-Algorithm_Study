from operator import is_


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
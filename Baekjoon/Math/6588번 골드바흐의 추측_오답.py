"""
6588번 - https://www.acmicpc.net/problem/6588

골드바흐의 추측
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.

예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 
또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.
백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

오답 이유
1. n까지의 소수를 전부 구해놓고 거기서 check을 하려 함
-> 시간 초과

2.for문을 3~n까지 돌릴 필요가 없었음
-> 이로 인해 소수로 덧셈이 안 되는 경우에 2배의 연산을 하게 됨 = 시간 초과

3. 소수 판별을 하는 for문은 sqrt(n)만큼만 돌리면 된다
-> https://coding-of-today.tistory.com/169
"""

def prime_number(num):   
    for i in range(3, int(num/2)+1, 2):  
        if num % i == 0:     
            return False           
    return True       

while True:
    n = int(input())
    if n == 0: break

    is_prime = False
    for i in range(3,int(n/2)+1,2):
        if prime_number(i) and prime_number(n-i):
            print(f"{n} = {i} + {n-i}")
            is_prime = True
            break
    
    if not is_prime:
        print("Goldbach's conjecture is wrong.")
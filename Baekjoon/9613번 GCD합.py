"""
9613번 - https://www.acmicpc.net/problem/9613 

GCD 합
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
"""

t = int(input())

## GCD: Greatest Common Divisor - Euclid Algorithm
def GCD(num1, num2):
    n = num2 % num1
    while(num1 != 0):
        n = num2 % num1
        num2 = num1
        num1 = n
    return num2

for i in range(t):
    num = list(map(int, input().split()))
    gcd = []
    
    for j in range(num[0]):
        for k in range(num[0]-1,j,-1):
            if num[j+1] > num[k+1]:
                gcd.append(GCD(num[k+1],num[j+1]))
            else:
                gcd.append(GCD(num[j+1],num[k+1]))
    print(sum(gcd))

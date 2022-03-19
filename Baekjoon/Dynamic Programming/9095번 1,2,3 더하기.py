"""
9095번 - https://www.acmicpc.net/problem/9095

1, 2, 3 더하기

정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
"""

T = int(input())

add_case = [0,1,2,4]

for i in range(4,11):
    tmp = add_case[i-1]+add_case[i-2]+add_case[i-3]
    add_case.append(tmp)

for _ in range(T):
    n = int(input())
    print(add_case[n])
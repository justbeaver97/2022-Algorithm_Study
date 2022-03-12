"""
11004번 - https://www.acmicpc.net/problem/11004

K번째 수
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.
"""

n = list(map(int, input().split()))
a = list(map(int, input().split()))

sorted_a = sorted(a)
print(sorted_a[n[1]-1])
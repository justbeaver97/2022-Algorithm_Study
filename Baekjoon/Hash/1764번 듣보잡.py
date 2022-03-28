"""
1764번 - https://www.acmicpc.net/problem/1764

듣보잡
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
people = {}
for i in range(N):
    name = input().rstrip()
    people[name] = i+1

compare_people = {}
for i in range(M):
    name = input().rstrip()
    compare_people[name] = i+1

answer, count = [], 0
for key in people:
    if key in compare_people:
        count += 1
        answer.append(key)
answer.sort()

print(count)
for name in answer:
    print(name)
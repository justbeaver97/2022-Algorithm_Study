"""
14225번 - https://www.acmicpc.net/problem/14225

부분수열의 합
수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.

예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다. 
하지만, 4는 만들 수 없기 때문에 정답은 4이다.

refercence
itertools.combinations - https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements 
"""

import itertools
from collections import Counter

n = int(input())
s = list(map(int, input().split()))

def sum_of_subsequence(array):
    combination = []
    for i in range(1, n+1):
        tmp = list(itertools.combinations(array, i))
        for j in tmp:
            combination.append(sum(j))
    return combination

def find_missing_num(array):
    i = 1
    for num in array:
        if num > i:
            break
        i += 1    
    print(i)

subsequence_s = sum_of_subsequence(s)
# print(subsequence_s)
sorted_s = sorted(subsequence_s)
# print(sorted_s)
# print(list(set(sorted_s)))
# find_missing_num(set(sorted_s))

check_num = [i for i in range(1, sorted_s[-1]+2)] 
result = Counter(check_num) - Counter(sorted_s) 
print(list(result.keys())[0])
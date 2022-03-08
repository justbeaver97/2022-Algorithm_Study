"""
14225번 - https://www.acmicpc.net/problem/14225

부분수열의 합
수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.

예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다. 
하지만, 4는 만들 수 없기 때문에 정답은 4이다.

refercence
itertools.combinations - https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements 
collections.Counter - https://velog.io/@kimdukbae/Python-collections-%EB%AA%A8%EB%93%88%EC%9D%98-Counter 
"""

import itertools
import  collections

n = int(input())
s = list(map(int, input().split()))

def sum_of_subsequence(array):
    combination = []
    for i in range(1, n+1):
        tmp = list(itertools.combinations(array, i))
        for j in tmp:
            combination.append(sum(j))
    return combination

subsequence_s = sum_of_subsequence(s)
sorted_s = sorted(subsequence_s)

compare = [i for i in range(1, sorted_s[-1]+2)] 
answer = collections.Counter(compare) - collections.Counter(sorted_s) 
print(list(answer.keys())[0])
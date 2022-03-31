"""
15904번 - https://www.acmicpc.net/problem/15904

UCPC는 무엇의 약자일까?
"""

import sys
input = sys.stdin.readline

sentence = input().rstrip()
ucpc, count = ['U','C','P','C'], 0
for alphabet in ucpc:
    if alphabet in sentence:
        count += 1
        sentence = sentence[sentence.index(alphabet)+1:]
    else: 
        print('I hate UCPC')
        break
if count == 4:
    print('I love UCPC')
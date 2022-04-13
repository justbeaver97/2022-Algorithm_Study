"""
9536번 - https://www.acmicpc.net/problem/9536

여우는 어떻게 울지?
"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sounds = list(input().split())
    animal_sound, fox_sounds = [], []

    while 1:
        animal = input().rstrip()
        if animal == "what does the fox say?":
            break
        animal_sound.append(animal.split()[-1])

    for sound in sounds:
        if sound not in animal_sound:
            fox_sounds.append(sound)

    for fox_sound in fox_sounds:
        print(fox_sound,end=' ')
    print()
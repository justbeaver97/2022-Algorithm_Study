"""
2751번 - https://www.acmicpc.net/problem/2751

수 정렬하기 2

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    front_arr = mergeSort(arr[mid:])
    back_arr = mergeSort(arr[:mid])
    
    merged_arr = []
    h, l = 0, 0
    while l < len(front_arr) and h < len(back_arr):
        if front_arr[l] < back_arr[h]:
            merged_arr.append(front_arr[l])
            l += 1
        else:
            merged_arr.append(back_arr[h])
            h += 1
    merged_arr += front_arr[l:]
    merged_arr += back_arr[h:]
    return merged_arr

N = int(input())
arr = [int(input()) for _ in range(N)]
merged = mergeSort(arr)
for num in merged:
    print(num)
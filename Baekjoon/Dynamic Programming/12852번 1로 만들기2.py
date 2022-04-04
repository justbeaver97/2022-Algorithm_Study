"""
12852번 - https://www.acmicpc.net/problem/12852

1로 만들기 2

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

reference
1. one-liner
https://dejavuqa.tistory.com/291

2. TypeError: 'int' object is not subscriptable
https://nov19.tistory.com/18 - 내가 5를 생성 안해놓고 6을 하려고 했음
"""

import sys
input = sys.stdin.readline

def print_answer(answer):
    print(answer[0])
    tmp = answer[1:][::-1]
    for num in tmp:
        print(num, end=' ')
    print()

N = int(input())
arr = [0]*(N+1)
arr[1] = [0,1]

if N==1:
    print_answer(arr[N])
elif N==2:
    arr[2] = [1,1,2]
    print_answer(arr[N])
elif N==3:
    arr[2],arr[3] = [1,1,2], [1,1,3]
    print_answer(arr[N])
else:
    arr[1],arr[2],arr[3] = [0,1], [1,1,2], [1,1,3]
    for i in range(4,len(arr)):
        ## 짝수일때
        if i % 2 == 0:
            i1, i2, i3 = arr[i-1][0], arr[i//2][0], N+1
            if i % 3 == 0:
                i3 = arr[i//3][0]

            if i1 < i2: count = i-1
            else:       count = i//2

            if i3 < arr[count][0]: count = i//3
            else:                  count = count

            arr[i] = arr[count][:]
            arr[i][0] = arr[count][0]+1
            arr[i].append(i)

        ## 홀수일때
        else:
            i1, i2, i3 = arr[i-1][0], N+1, N+1
            if i % 2 == 0:
                i2 = arr[i//2][0]
            if i % 3 == 0:
                i3 = arr[i//3][0]

            if i1 < i2: count = i-1
            else:       count = i//2

            if i3 < arr[count][0]: count = i//3
            else:                  count = count

            arr[i] = arr[count][:]
            arr[i][0] = arr[count][0]+1
            arr[i].append(i)
    print_answer(arr[N])
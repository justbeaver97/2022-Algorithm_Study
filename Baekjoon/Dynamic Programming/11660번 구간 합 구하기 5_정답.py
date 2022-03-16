"""
11660번 - https://www.acmicpc.net/problem/11660

구간 합 구하기 5

NxN개의 수가 NxN 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.
예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.
여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.
표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

오답이유
1. 답을 바로 출력하면 되는데, 한번 answers에 append하고 이를 for문을 사용해서 다시 출력
2. python3 사용 -> pypy 사용시 해결
"""

n, m = map(int, input().split())

arr= []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

add_range = []
for i in range(m):
    tmp = list(map(int, input().split()))
    add_range.append(tmp)


sum = [0]*(n*n)
for i in range(n):
    for j in range(n):
        if j+i*n != 0:
            sum[j+i*n] = sum[(j+i*n)-1] + arr[i][j]
        else: 
            sum[j+i*n] = arr[i][j]

# answers = []
for i in range(m):
    tmp_answer = 0
    for j in range(n):
        if j >= add_range[i][0]-1 and j<= add_range[i][2]-1:
            if j*n+add_range[i][1]-2 < 0:
                tmp = sum[j*n+add_range[i][3]-1]
                tmp_answer += tmp
            else:
                tmp = sum[j*n+add_range[i][3]-1] - sum[j*n+add_range[i][1]-2]
                tmp_answer += tmp
    print(tmp_answer)
    # answers.append(tmp_answer)

# for answer in answers:
#     print(answer)
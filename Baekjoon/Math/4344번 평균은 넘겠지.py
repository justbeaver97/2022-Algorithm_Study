"""
4344번 - https://www.acmicpc.net/problem/4344

평균은 넘겠지 
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
"""

c = int(input())
answer = []
for _ in range(c):
    tmp = list(map(int, input().split()))

    sum = 0
    for i in range(1, len(tmp)):
        sum += tmp[i]
    average = sum/tmp[0]
    
    cnt = 0
    for i in range(1, len(tmp)):
        if tmp[i]>average:
            cnt += 1
    answer.append((cnt/tmp[0])*100)
    
for i in range(len(answer)):
    print(f"{answer[i]:.3f}%")
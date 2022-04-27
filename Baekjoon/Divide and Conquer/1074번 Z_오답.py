"""
1074번 - https://www.acmicpc.net/problem/1074

Z

처음에 못 푼 이유:
tmp_i와 j를 2**(N-i) 만큼 더하거나 빼줘야하는데
이를 0*(2**(N-i+2)//4) + 2**(N-i) 로 다시 선언
n<=3 일때는 이에 대해 티가 나지 않았지만, 그 이후부터는 달라지기 시작

오답 이유: 시간초과
이유를 모르겠음. 동일하게 사분면 분할로 풀었고, 오답 정답 방법을 둘 다 생각했다가
이 방법을 선택했는데 시간 초과가 남. 애초에 생각했던 방법이 있었기에 정답 방식으로 진행.
"""

import sys
input = sys.stdin.readline

N, r, c = map(int,input().split())
divided, tmp_i, tmp_j, answer = [0], 2**(N-1), 2**(N-1), 0

for i in range(1,N):
    if i != 1:
        if divided[i-1] == 0: 
            tmp_i -= 2**(N-i)
            tmp_j -= 2**(N-i)
        elif divided[i-1] == 1:
            tmp_i -= 2**(N-i) 
            tmp_j += 1*(2**(N-i+2)//4)
        elif divided[i-1] == 2:
            tmp_i += 1*(2**(N-i+2)//4)
            tmp_j -= 2**(N-i)
        elif divided[i-1] == 3:
            tmp_i += 1*(2**(N-i+2)//4)
            tmp_j += 1*(2**(N-i+2)//4)

    if tmp_i<=r and tmp_j<=c:  divided.append(3)
    elif tmp_i<=r and tmp_j>c: divided.append(2)
    elif tmp_i>r and tmp_j<=c: divided.append(1)
    else:                      divided.append(0)

for i in range(len(divided)):
    answer += divided[i] * (2**((len(divided)-i)*2))
if (r+c) % 2 == 0:
    if r % 2 == 0: print(answer)
    else:          print(answer+3)
else:
    if r % 2 == 0 and c % 2 != 0: print(answer+1)
    else:                         print(answer+2)
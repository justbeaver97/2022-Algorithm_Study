"""
21610번 - https://www.acmicpc.net/problem/21610

마법사 상어와 비바라기(삼성 2021 상반기 코딩테스트 1번 문제)
"""

n, m = map(int, input().split())

water = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    water.append(tmp)

order = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    order.append(tmp)

real_cloud = [[0]*n for _ in range(n)]
real_cloud[n-1][0],real_cloud[n-1][1],real_cloud[n-2][0],real_cloud[n-2][1] = 1, 1, 1, 1

## direction of the cloud - x와 y가 반대로 되어야함(내 기준과 문제의 기준이 반대되기 때문)
cloud_dir_y = [-1,-1,0,1,1,1,0,-1]
cloud_dir_x = [0,-1,-1,-1,0,1,1,1]

for i in range(m):
    ## 구름이 이동한 방향을 저장하기 위한 tmp_cloud
    tmp_cloud = [[0]*n for _ in range(n)]

    ## 1. 모든 구름이 d_i 방향으로 s_i 칸 이동한다.
    for j in range(n):
        for k in range(n):
            if real_cloud[j][k] == 1:
                real_cloud[j][k] = 0
                new_x = j + cloud_dir_x[order[i][0]-1]*order[i][1]
                new_y = k + cloud_dir_y[order[i][0]-1]*order[i][1]
                
                ## 이동 횟수가 -5 or 10을 넘어갈 수도 있으므로 나눈 몫의 절댓값을 취해서 곱해준다
                if new_x < 0:
                    new_x += n*abs((new_x//n)) 
                elif new_x >= n:
                    new_x -= n*abs((new_x//n))
                if new_y < 0:
                    new_y += n*abs((new_y//n))
                elif new_y >= n:
                    new_y -= n*abs((new_y//n))

                tmp_cloud[new_x][new_y] = 1
    real_cloud = tmp_cloud[:]

    ## 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for j in range(n):
        for k in range(n):
            if real_cloud[j][k] == 1:
                water[j][k] += 1

    ## 3. 구름이 모두 사라진다 
    ## 이때 원래 구름의 위치는 tmp_cloud에 남아있기 때문에 real_cloud를 초기화 해주어도 상관이 없다
    real_cloud = [[0]*n for _ in range(n)]

    ## 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다
    for j in range(n):
        for k in range(n):
            if tmp_cloud[j][k] == 1:
                if j == 0:
                    if k == 0:
                        if water[j+1][k+1] > 0: water[j][k] += 1
                    elif k == n-1:
                        if water[j+1][k-1] > 0: water[j][k] += 1
                    else: 
                        if water[j+1][k-1] > 0: water[j][k] += 1
                        if water[j+1][k+1] > 0: water[j][k] += 1
                elif j != 0 and k == 0:
                    if j == n-1:
                        if water[j-1][k+1] > 0: water[j][k] += 1
                    else:
                        if water[j-1][k+1] > 0: water[j][k] += 1
                        if water[j+1][k+1] > 0: water[j][k] += 1
                elif j != 0 and k == n-1:
                    if j == n-1:
                        if water[j-1][k-1] > 0: water[j][k] += 1
                    else:
                        if water[j+1][k-1] > 0: water[j][k] += 1
                        if water[j-1][k-1] > 0: water[j][k] += 1
                elif k != 0 and k != n-1 and j == n-1:
                    if water[j-1][k+1] > 0: water[j][k] += 1
                    if water[j-1][k-1] > 0: water[j][k] += 1
                else:
                    if water[j+1][k-1] > 0: water[j][k] += 1
                    if water[j+1][k+1] > 0: water[j][k] += 1
                    if water[j-1][k-1] > 0: water[j][k] += 1
                    if water[j-1][k+1] > 0: water[j][k] += 1

    ## 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 
    ## 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for j in range(n):
        for k in range(n):
            if water[j][k] > 1 and tmp_cloud[j][k] != 1:
                water[j][k] -= 2
                real_cloud[j][k] = 1

sum = 0
for i in range(n):
    for j in range(n):
        sum += water[i][j]
print(sum)
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

# direction of the cloud
cloud_dir_y = [-1,-1,0,1,1,1,0,-1]
cloud_dir_x = [0,-1,-1,-1,0,1,1,1]

for i in range(m):
    tmp_cloud = [[0]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if real_cloud[j][k] == 1:
                real_cloud[j][k] = 0
                new_x = j + cloud_dir_x[order[i][0]-1]*order[i][1]
                new_y = k + cloud_dir_y[order[i][0]-1]*order[i][1]
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

    for j in range(n):
        for k in range(n):
            if real_cloud[j][k] == 1:
                water[j][k] += 1

    for j in range(n):
        for k in range(n):
            if real_cloud[j][k] == 1:
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

    ## 비가 전부 내리고 난 뒤에는 구름 사라짐
    real_cloud = [[0]*n for _ in range(n)]

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
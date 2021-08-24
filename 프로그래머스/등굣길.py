def solution(m, n, puddles):
    answer = 0
    road = [[0]*m for _ in range(n)]
    # print(road)
    for pud in puddles:
        road[pud[1]-1][pud[0]-1] = -1
    road[0][0] = 1
    for i in range(n):
        for j in range(m):
            if road[i][j] >= 0:
                if i >= 1 and road[i-1][j]>0:
                    road[i][j] += road[i-1][j]
                if j >= 1 and road[i][j-1]>0:
                    road[i][j] += road[i][j-1]
    for i in range(n):
        print(road[i])
    answer = road[n-1][m-1]

    return answer


# solution(4,3,[[2, 2]])
solution(4,3,[[1, 2]])
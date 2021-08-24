def solution(game_board, table):
    dx = [0,1,0,-1] # 오른쪽 아래 왼쪽 위
    dy = [1,0,-1,0]
    ln = len(table)
    total_cnt = 0
    for t in range(4):
        b_visited = [[0 for _ in range(ln)] for _ in range(ln)]
        b_routes = []
        for i in range(ln):
            for j in range(ln):
                b_route = [[i,j,0]]
                if game_board[i][j] == 0 and b_visited[i][j] == 0:
                    flag = 0
                    stack = [[i,j]]
                    b_visited[i][j] = 1
                    while stack:
                        a,b = stack.pop()
                        
                        for k in range(4):
                            A = a + dx[k]
                            B = b + dy[k]
                            if 0 <= A <= ln-1 and 0 <= B <= ln-1 and game_board[A][B] == 0 and b_visited[A][B] ==0:
                                flag = 1
                                b_visited[A][B] = 1
                                b_route.append([A,B,0])
                                stack.append([A,B])
                    if len(b_route) == 1 and flag == 0:
                        b_routes.append(b_route)
                    if len(b_route) > 1:
                        b_routes.append(b_route)


        visited = [[0 for _ in range(ln)] for _ in range(ln)]
        routes = []
        for i in range(ln):
            for j in range(ln):
                route = [[i,j,0]]
                if table[i][j] == 1 and visited[i][j] == 0:
                    flag = 0
                    stack = [[i,j]]
                    visited[i][j] = 1
                    while stack:
                        a,b = stack.pop()
                        for k in range(4):
                            A = a + dx[k]
                            B = b + dy[k]
                            if 0 <= A <= ln-1 and 0 <= B <= ln-1 and table[A][B] == 1 and visited[A][B] ==0:
                                flag = 1
                                visited[A][B] = 1
                                route.append([A,B,0])
                                stack.append([A,B])
                    if len(route) == 1 and flag == 0:
                        routes.append(route)
                    if len(route) > 1:
                        routes.append(route)

        for b_r in b_routes:
            for r in routes:
                if len(b_r) == len(r) == 1:
                    if game_board[b_r[0][0]][b_r[0][1]] == 0 and b_r[0][2] == 0 and r[0][2] == 0:
                        game_board[b_r[0][0]][b_r[0][1]] = 1
                        table[r[0][0]][r[0][1]] = 0
                        b_r[0][2] = 1
                        r[0][2] = 1
                        total_cnt += 1
                        
                elif len(b_r) == len(r) != 1 and b_r[0][2] == 0 and r[0][2] == 0 :# 2번위치는 visited
                    if game_board[b_r[0][0]][b_r[0][1]] == 0:
                        a = b_r[0][0]-r[0][0]
                        b = b_r[0][1]-r[0][1]
                        cnt = 1
                        for i in range(1,len(r)):
                            if b_r[i][0]-r[i][0] == a and b == b_r[i][1]-r[i][1]:
                                cnt += 1
                        if cnt == len(b_r):
                            total_cnt += cnt
                            for l in range(len(r)):
                                b_r[l][2] = 1
                                r[l][2] = 1
                            for b_ri in b_r:
                                game_board[b_ri[0]][b_ri[1]] = 1
                            for ri in r:
                                table[ri[0]][ri[1]] = 0
        table = [list(reversed(i)) for i in zip(*table)]

    return total_cnt
# solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
# solution([[0,0,1,1],
#           [1,0,1,0],
#           [0,1,0,0],
#           [0,0,1,1]],

#           [[1,1,0,0],
#            [0,1,0,1],
#            [1,0,1,1],
#            [1,1,0,0]])
# solution([      [0, 0, 0, 0, 0],
#                 [1, 1, 1, 0, 1],
#                 [0, 0, 1, 1, 1],
#                 [0, 0, 1, 1, 0],
#                 [0, 0, 1, 1, 1]],

#                [[1, 0, 0, 0, 1],
#                 [1, 1, 0, 0, 0],
#                 [1, 0, 0, 1, 1],
#                 [1, 0, 0, 1, 1],
#                 [1, 0, 0, 1, 1]])
# solution([[1, 1, 1, 1, 1, 0],
#           [0, 0, 0, 0, 1, 0],
#           [1, 1, 1, 1, 1, 0],
#           [0, 0, 1, 1, 1, 0],
#           [1, 1, 0, 1, 1, 1],
#           [1, 1, 0, 1, 0, 0]],

#           [[0, 1, 0, 0, 1, 1],
#           [0, 1, 0, 1, 0, 0],
#           [0, 1, 0, 1, 0, 1], 
#           [0, 1, 0, 1, 0, 1],
#           [0, 0, 0, 1, 0, 0],
#           [0, 0, 0, 0, 0, 0]])

# solution([
# [0,0,0,0,0,0,1,0,1,0,0,0],
# [1,1,1,1,1,1,0,0,0,1,0,0],
# [0,0,0,0,0,1,0,1,0,1,1,0],
# [1,0,1,1,1,0,1,0,1,0,0,1],
# [0,1,0,0,0,0,1,0,1,0,0,0],
# [0,0,1,1,1,0,1,0,1,1,0,1],
# [0,1,0,0, 0, 1, 1, 0, 0, 0, 1, 0], 
# [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], 
# [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], 
# [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], 
# [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], 
# [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
# [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], 
# [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], 
# [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], 
# [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], 
# [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], 
# [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
# [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], 
# [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], 
# [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]])

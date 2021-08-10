N = int(input())

data = [list(map(int,input().split())) for _ in range(N)]
numbers = []
for i in range(len(data)):
    for j in range(len(data[i])):
        numbers.append(data[i][j])
numbers.append(0)
num = list(set(numbers))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
minnumber = 0
for n in num:
    data0 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] <= n:
                data0[i][j] = 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if data0[i][j] == 0:
                stack = [[i,j]]
                cnt += 1

                while(stack):
                    a,b = stack.pop()
                    data0[a][b] = 1
                    for k in range(4):
                        A = a + dy[k]
                        B = b + dx[k]
                        if 0 <= A <= N-1 and 0 <= B <= N-1 and data0[A][B] == 0:
                            stack.append([A,B])
    if minnumber < cnt:
        minnumber = cnt
print(minnumber)

    






from collections import deque

F,S,G,U,D = list(map(int,input().split()))

visited = [0] * (F+1)
visited[S] = 1
queue= deque([[S,0]])
flag = 0
while(queue):
    s,cnt = queue.popleft()
    if s == G:
        flag = 1
        break
    cnt+=1
    if s-D >= 1 and not visited[s-D]:
        visited[s-D] = 1
        queue.append([s-D,cnt])
    if s+U <= F and not visited[s+U]:
        visited[s+U] = 1
        queue.append([s+U,cnt])

if flag == 1:
    print(cnt)
else:
    print("use the stairs")



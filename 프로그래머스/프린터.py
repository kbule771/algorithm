from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    index = deque([])
    for i in range(len(priorities)):
        index.append(i)
    result = []
    while(index):
        a = priorities.popleft()
        b = index.popleft()
        if priorities:
            if a < max(priorities):
                priorities.append(a)
                index.append(b)
            else:
                result.append([a,b])
        else:
            result.append([a,b])
    for i in range(len(result)):
        if result[i][1] == location:
            return i+1
            
    
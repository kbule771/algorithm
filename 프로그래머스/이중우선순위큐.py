import heapq

def solution(operations):
    answer = []
    data = []
    for oper in operations:
        a,b = oper.split(' ')
        if a == 'I':
            heapq.heappush(data, int(b))
        else:
            if data:
                if b == '-1':
                    heapq.heappop(data)
                else:
                    data.pop()
        # print(data)
    data = sorted(data)
    if data:
        answer.append([data[-1],data[0]])
    else:
        answer.append([0,0])
    # print(answer)
    return answer[0]

solution(["I 16","D 1"])
solution(["I 7","I 5","I -5","D -1"])